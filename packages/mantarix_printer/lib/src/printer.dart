import 'dart:io';
import 'dart:convert';

import 'package:mantarix/mantarix.dart';
import 'package:flutter/widgets.dart';
import 'package:printing/printing.dart';
import '../utils/printer.dart';

class PrinterControl extends StatefulWidget {
  final Control? parent;
  final Control control;
  final Widget? nextChild;
  final MantarixControlBackend backend;

  const PrinterControl(
      {super.key,
      required this.parent,
      required this.control,
      required this.nextChild,
      required this.backend});

  @override
  State<PrinterControl> createState() => _PrinterControlState();
}

class _PrinterControlState extends State<PrinterControl> {
  late final PrintingInfo info;

  @override
  void initState() {
    super.initState();
    _loadPrintingInfo();
  }

  Future<void> _loadPrintingInfo() async {
    info = await Printing.info();
    _subscribeMethods();
    setState(() {});
  }

  void _subscribeMethods() {
    widget.backend.subscribeMethods(widget.control.id,
        (methodName, args) async {
      switch (methodName) {
        case "print":
          try {
            if (info.canPrint == false) {
              return "printing is not supported on this platform!";
            }
            final String? filePath = args['filePath'];
            if (filePath == null) return "filePath is null";
            final file = File(filePath);
            final bytes = await file.readAsBytes();
            await Printing.layoutPdf(
              onLayout: (format) async => bytes,
              name: args['name'] ?? 'Document',
              format: parsePdfPageFormat(format: args['format']),
              dynamicLayout: parseBool(args['dynamicLayout']) ?? true,
              usePrinterSettings: parseBool(args['usePrinterSettings']) ?? false,
              outputType: parseOutputType(type: args['type']),
              forceCustomPrintPaper: parseBool(args['forceCustomPrintPaper']) ?? false
            );
            return "ok";
          } on Exception catch (e) {
            return "$e";
          }
        case "directprint":
          try {
            if (info.directPrint == false) {
              return "printing is not supported on this platform!";
            }
            if (args['printer'] == null) return "printer is null";
            final String? filePath = args['filePath'];
            if (filePath == null) return "filePath is null";
            final file = File(filePath);
            final bytes = await file.readAsBytes();
            await Printing.directPrintPdf(
              printer: Printer.fromMap(json.decode(args['printer']!)),
              onLayout: (format) async => bytes,
              name: args['name'] ?? 'Document',
              format: parsePdfPageFormat(format: args['format']),
              dynamicLayout: parseBool(args['dynamicLayout']) ?? true,
              usePrinterSettings: parseBool(args['usePrinterSettings']) ?? false,
              outputType: parseOutputType(type: args['type']),
              forceCustomPrintPaper: parseBool(args['forceCustomPrintPaper']) ?? false
            );
            return "ok";
          } on Exception catch (e) {
            return "$e";
          }
        case "pickprinter":
          try {
            if (info.canListPrinters == false) {
              return "printing is not supported on this platform!";
            }
            if (!mounted) return "widget is disposed";
            Printer? picked = await Printing.pickPrinter(context: context);
            if (picked == null) return "no printer selected";
            return json.encode(picked.toMap());
          } on Exception catch (e) {
            return "$e";
          }
        case "getlistofprinters":
          return await printersToJson();
        case "share":
          try {
            if (info.canShare == false) {
              return "printing is not supported on this platform!";
            }
            final String? filePath = args['filePath'];
            if (filePath == null) return "filePath is null";
            final file = File(filePath);
            final bytes = await file.readAsBytes();
            await Printing.sharePdf(
              bytes: bytes,
              filename: args['name'] ?? 'Document.pdf',
              subject: args['subject'],
              body: args['body']
            );
            return "ok";
          } on Exception catch (e) {
            return "$e";
          }
      }
      return null;
    });
  }

  @override
  Widget build(BuildContext context) {
    debugPrint("PrinterControl build: ${widget.control.id}");
    return const SizedBox.shrink();
  }

  Future<String> printersToJson() async {
    if (!info.canListPrinters) {
      return "printing is not supported on this platform!";
    }
    final printers = await Printing.listPrinters();
    final result = printers.map((p) => p.toMap()).toList();
    return json.encode(result);
  }

}
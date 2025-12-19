import 'package:printing/printing.dart';
import 'package:collection/collection.dart';
import 'package:pdf/pdf.dart';

PdfPageFormat parsePdfPageFormat({String? format, PdfPageFormat defaultValue=PdfPageFormat.standard}) {
  if (format == null) {
    return defaultValue;
  }
  switch (format.toLowerCase()) {
    case 'a3':
      return PdfPageFormat.a3;
    case 'a4':
      return PdfPageFormat.a4;
    case 'a5':
      return PdfPageFormat.a5;
    case 'a6':
      return PdfPageFormat.a6;
    case 'letter':
      return PdfPageFormat.letter;
    case 'legal':
      return PdfPageFormat.legal;
    case 'roll57':
      return PdfPageFormat.roll57;
    case 'roll80':
      return PdfPageFormat.roll80;
    case 'standard':
      return PdfPageFormat.standard;
    case 'undefined':
      return PdfPageFormat.undefined;
    default:
      return defaultValue;
  }
}

OutputType parseOutputType({String? type, OutputType defaultValue=OutputType.generic}) {
  if (type == null) {
    return defaultValue;
  }
  return OutputType.values.firstWhereOrNull(
          (e) => e.name.toLowerCase() == type.toLowerCase()) ??
      defaultValue;
}
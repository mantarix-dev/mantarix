import 'package:flutter/widgets.dart';
import 'package:mantarix/src/utils/others.dart';

import '../mantarix_control_backend.dart';
import '../models/control.dart';
import '../utils/alignment.dart';
import 'create_control.dart';
import 'scroll_notification_control.dart';
import 'scrollable_control.dart';
import 'block_scroll_notification.dart';

final ValueNotifier<bool> _blockParentScrollNotifier = ValueNotifier(false);

class ColumnControl extends StatelessWidget {
  final Control? parent;
  final Control control;
  final bool parentDisabled;
  final bool? parentAdaptive;
  final List<Control> children;
  final MantarixControlBackend backend;

  const ColumnControl(
      {super.key,
      this.parent,
      required this.control,
      required this.children,
      required this.parentDisabled,
      required this.parentAdaptive,
      required this.backend});

  @override
  Widget build(BuildContext context) {
    debugPrint("Column build: ${control.id}");

    final spacing = control.attrDouble("spacing", 10)!;
    final mainAlignment = parseMainAxisAlignment(
        control.attrString("alignment"), MainAxisAlignment.start)!;
    bool tight = control.attrBool("tight", false)!;
    bool wrap = control.attrBool("wrap", false)!;
    bool disabled = control.isDisabled || parentDisabled;
    bool? adaptive = control.attrBool("adaptive") ?? parentAdaptive;
    ScrollMode scrollMode = parseScrollMode(control.attrString("scroll"), ScrollMode.none)!;

    List<Widget> controls = [];

    bool firstControl = true;
    for (var ctrl in children.where((c) => c.isVisible)) {
      // spacer between displayed controls
      if (!wrap &&
          spacing > 0 &&
          !firstControl &&
          mainAlignment != MainAxisAlignment.spaceAround &&
          mainAlignment != MainAxisAlignment.spaceBetween &&
          mainAlignment != MainAxisAlignment.spaceEvenly) {
        controls.add(SizedBox(height: spacing));
      }
      firstControl = false;

      // displayed control
      controls.add(
          createControl(control, ctrl.id, disabled, parentAdaptive: adaptive));
    }

    Widget child = wrap
        ? Wrap(
            direction: Axis.vertical,
            spacing: spacing,
            runSpacing: control.attrDouble("runSpacing", 10)!,
            alignment: parseWrapAlignment(
                control.attrString("alignment"), WrapAlignment.start)!,
            crossAxisAlignment: parseWrapCrossAlignment(
                control.attrString("horizontalAlignment"),
                WrapCrossAlignment.start)!,
            children: controls,
          )
        : Column(
            mainAxisAlignment: mainAlignment,
            mainAxisSize: tight ? MainAxisSize.min : MainAxisSize.max,
            crossAxisAlignment: parseCrossAxisAlignment(
                control.attrString("horizontalAlignment"),
                CrossAxisAlignment.start)!,
            children: controls,
          );
    if (scrollMode == ScrollMode.none) {
      child = ScrollableControl(
          control: control,
          scrollDirection: wrap ? Axis.horizontal : Axis.vertical,
          backend: backend,
          parentAdaptive: adaptive,
          child: child,
      );
    }
    else {
      child = NotificationListener<BlockParentScrollNotification>(
        onNotification: (notification) {
          if (_blockParentScrollNotifier.value != notification.block) {
            _blockParentScrollNotifier.value = notification.block;
          }
          return true;
        },
        child: ValueListenableBuilder<bool>(
          valueListenable: _blockParentScrollNotifier,
          child: child,
          builder: (context, block, child) {
            return ScrollableControl(
                control: control,
                scrollDirection: wrap ? Axis.horizontal : Axis.vertical,
                backend: backend,
                parentAdaptive: adaptive,
                physics: _blockParentScrollNotifier.value ? const NeverScrollableScrollPhysics() : null,
                child: child!,
            );
          },
        ),
      );
    }

    if (control.attrBool("onScroll", false)!) {
      child = ScrollNotificationControl(
          control: control, backend: backend, child: child);
    }

    return constrainedControl(context, child, parent, control);
  }
}

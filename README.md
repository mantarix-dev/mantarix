# Mantarix

<img src="media/loading-animation.png" width="50%"/>

## Mantarix structure
Mantarix follows the Flet architecture. Its differences in the core and build tools are the addition of layers of obfuscation in compiling Python application code and managing extensions and building local modules specific to each specific version of the project.

### Mantarix components
``Mantarix Extensions``: This is a section for managing input extensions. When a task imports an extension from Mantarix packages into its application code, Mantarix automatically detects it and adds it to the local compilation of Mantarix's internal packages. This allows for better management of extensions and input packages to the module. It is accessible via `import mantarix.extensions.{extension_name}`


``Mantarix Translator``: It is a section for supporting and managing different languages ​​in the user application, which can be activated if necessary. This tool helps the user application UI to be translated and switched to any language and uses 2 translators, google translate and mymemory, which can be configured. It is accessible via `import mantarix.translator`


``Mantarix Obfuscator``: This section is used to obfuscate the Python source code of the user application at build time. In this case, the source code of your project's Python files is obfuscated and then converted to `.pyc` files and placed in the project. It is accessible via `mantarix build {platform} --obfuscate`


## Mantarix app example

```python title="counter.py"
import mantarix as mx

def main(page: mx.Page):
    page.title = "Mantarix counter example"
    page.vertical_alignment = mx.MainAxisAlignment.CENTER

    txt_number = mx.TextField(value="0", text_align=mx.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        mx.Row(
            [
                mx.IconButton(mx.Icons.REMOVE, on_click=minus_click),
                txt_number,
                mx.IconButton(mx.Icons.ADD, on_click=plus_click),
            ],
            alignment=mx.MainAxisAlignment.CENTER,
        )
    )

mx.app(main)
```

run this for install `mantarix` module:

```bash
pip install mantarix[all]
```

and run the program:

```bash
python counter.py
```
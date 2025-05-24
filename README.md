## fm3chanic Themes for Windows Terminal

This repository contains all color themes for the Windows Terminal I've created.
You can find a HTML scheme file for all the color themes in this repository: https://github.com/fm3chanic/color_schemes

### Installation:

1. Download the [...]theme file and the [...]scheme file or copy them in a text editor of choice.
2. Open the `settings.json` file from Windows Terminal
3. In the `schemes` section of the file, paste the contents of the your scheme file (e.g. `naruto_sakura_haruno_dark_scheme.json`)
4. Search for the `themes` section and paste the contents of the corresponding theme file (e.g. `naruto_sakura_haruno_dark_theme.json`).
5. Update `colorScheme` within the `profiles` section to include your chosen scheme:

    ```json
    {
        "profiles": {
            "defaults": {
                "colorScheme": "sakura-haruno-dark"
            }
        }
    }
    ```

5. Update `theme` to use your chosen theme:

    ```json
    {
        "theme": "sakura-haruno-dark"
    }
    ```
### Contribution:

I accept all fixes, required updates, etc.
Please use colors from the according color scheme for this. You can find these in the repo linked above.
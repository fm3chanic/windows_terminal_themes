## fm3chanic Themes for Windows Terminal

This repository contains all color themes for the Windows Terminal I've created.
You can find a HTML scheme file for all the color themes in this repository: https://github.com/fm3chanic/color_schemes

HTML-scheme files for all color themes: https://github.com/fm3chanic/color_schemes

Further information regarding the Vtuber project: https://github.com/fm3chanic/vtuber_project

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

If you want to help maintaining the themes, please use colors from the according color scheme. You can find the scheme files in the repo linked above.
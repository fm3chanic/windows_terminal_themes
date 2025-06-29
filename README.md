## fm3chanic Themes for Windows Terminal

This repository contains all color themes for the Windows Terminal I've created so far.<br>
Themes which have been created during my project of color theming Vtubers are in the folder "vtuber_project". The folder "other" contains all color themes which where created outside of the project.

**[HTML Reference Sheets & Galery Non-Project Themes](https://github.com/fm3chanic/color_schemes)**<br>
**[Vtuber Project | Information & Galery](https://github.com/fm3chanic/vtuber_project)**

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
	
> [!TIP]
> The application reads the whole `settings.json` every time you save. To avoid error messages only save when you copied both parts of the theme.

### Contribution:

If you want to help maintaining the themes, please use colors from the according color scheme. You can find the scheme files in the repo linked above.

---

# Multi-Language and Theme Switcher in PyQt5

This is a PyQt5 desktop application that demonstrates how to implement **multi-language support**, **light/dark mode switching**, **font switching**, and **date formatting** (Gregorian, Jalali, and Hijri). The application is designed to support dynamic language switching and theme switching at runtime.

## Features:

* **Multi-language Support**: The app supports different languages (English, Persian, Arabic, etc.) with RTL (Right-to-Left) and LTR (Left-to-Right) support based on language.
* **Light/Dark Mode Toggle**: Switch between light and dark themes using `.qss` stylesheets.
* **Font Switching**: Dynamically change fonts within the app.
* **Date Formatting**: Show the date in Gregorian, Jalali, or Hijri formats.

## Requirements:

Before running the app, make sure you have the following dependencies installed:

* **PyQt5**
* **jdatetime** (for Jalali date conversion)
* **hijri-converter** (for Hijri date conversion)

### Install the dependencies:

```bash
pip install PyQt5 jdatetime hijri-converter
```

## Project Structure

```
your_project/
├── main.py                # Main PyQt5 app file
├── translations.json      # JSON file for language translations
├── themes/                # Theme styles (light and dark modes)
│   ├── dark.qss           # Dark mode stylesheet
│   └── light.qss          # Light mode stylesheet
```

* **translations.json** contains language translations in different languages (e.g., English, Persian, Arabic).
* **themes/** directory contains two QSS files: one for light mode (`light.qss`) and one for dark mode (`dark.qss`).

## How to Use the Application

1. **Run the app**:

   * In your terminal, navigate to your project directory.
   * Run the `main.py` file using Python:

   ```bash
   python main.py
   ```

2. **Change Language**:

   * You can dynamically change the language by calling the `Translator` class with a new language key (e.g., `'en'`, `'fa'`, `'ar'`).
   * The app will automatically update text and layout (LTR/RTL).

3. **Switch Themes**:

   * The theme can be switched between **light mode** and **dark mode** at runtime. The change is immediate and does not require restarting the app.

4. **Switch Fonts**:

   * The font of the application can be changed at runtime by selecting a new font from the available options.

5. **Date Formatting**:

   * The app supports three types of date formatting:

     * **Gregorian**: Standard format
     * **Jalali**: Persian calendar format (using `jdatetime`)
     * **Hijri**: Islamic calendar format (using `hijri-converter`)

---

## Code Walkthrough

1. **Main Window**:

   * The main window contains labels and buttons to demonstrate language switching, date formatting, theme switching, and font changing.

2. **Translation System**:

   * The `Translator` class loads translations from a `translations.json` file.
   * It dynamically updates all UI elements based on the selected language.

3. **Theme Switching**:

   * The `apply_theme()` method loads a `.qss` stylesheet depending on the selected theme (light or dark).

4. **Date Formatting**:

   * The `update_date()` method formats the current date based on the selected format (Gregorian, Jalali, or Hijri).

5. **Font Switching**:

   * The app dynamically changes the font used in the UI using `QFont`.

---

## Example Usage

* **Switching language to Persian**:

  * The app can switch to Persian by setting the language key to `'fa'`.

* **Switching to Dark Mode**:

  * The theme can be switched to dark mode by selecting the dark theme.

---

## License

This project is open-source and available under the MIT License.

---

# Repository Usage Instructions

1. **Install dependencies**

   - Run `env.bat` to automatically create and activate a virtual environment and install all required libraries.

2. **Process your images**

   - To process images, simply drag and drop your folder with files onto `Process.bat` or run it without arguments to process the current directory.
   - Please note, images must be with integers numaration without any symbols
     (must be: 1.png-100.png, not aasdh%@\_001.png-[randomstaff]\_100.png)
   - The script will automatically perform all steps: combine, resize, crop, and compress.

3. **Example processing**

   - To test the repository, run `start_example.bat`. It will process the example and offer to upload the result to your Steam Workshop.

4. **Upload to Steam Workshop**

   - To upload results to Steam, use `Upload.bat` or the corresponding step in `start_example.bat`.
   - You can drag and drop a folder for upload or run the batch file without arguments to upload from the current directory.

5. **Requirements**

   - Python 3.10+
     `winget install Python.Python.3.10`
   - Steam account for uploading to Workshop

6. **Additional info**
   - All scripts are located in the `scripts` folder.
   - Configuration and helper modules are in the `modules` folder.

**Steam Workshop:**
If you log in through the webdriver, cookies will be saved in `cookies.json` so you do not need to log in again.

**Disclaimer:**
I am not responsible for the security of your Steam account. If you want to remove saved cookies, simply delete the `cookies.json` file from the project directory.

If you have any questions, check the README or open an Issue!

**Manual upload to Steam Workshop:**
If you want to manually upload your images, go to https://steamcommunity.com/sharedfiles/edititem/767/3 and use the following code in your browser console:

```
v_trim=_=>{return _},$J('#title').val(' \n'+Array.from(Array(126),_=>'\t').join(''));$J('[name=consumer_app_id]').val(480);$J('[name=file_type]').val(0);$J('[name=visibility]').val(0);
```

You do not need to enter an image name, just click the publish button. Repeat this process 5 times for each cropped image in the `upload` folder.

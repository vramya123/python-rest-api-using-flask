While running in windows, please follow below steps:-

Step 1:- Activate a Virtual Environment in VS Code
- Open the Integrated Terminal
- Use the shortcut: Ctrl + `` (backtick), or
- Go to View > Terminal
- Create a Virtual Environment (if you haven’t yet)
In the terminal, run:
python -m venv .venv
- Activate the Environment
Depending on your OS and shell:
| - Shell
 | - Command to Activate
 | 
| - PowerShell
 | - . .\.venv\Scripts\Activate.ps1
 | 
| - Command Prompt
 | - .venv\Scripts\activate.bat
 | 
| - Git Bash
 | - source .venv/Scripts/activate
 | 
| - macOS/Linux
 | - source .venv/bin/activate
 | 

Step 2: Tell VS Code to Use It
- Press Ctrl + Shift + P to open the Command Palette
- Type and select “Python: Select Interpreter”
- Choose the one that points to .venv

Step 3:- Set environment variable(these need to ne set each time terminal is opened)
-$env:FLASK_APP = "application.py"                                         
-$env:FLASK_ENV = "development" 

Step 4: Run flask
- python -m flask run

Step5: To add entry into DB , follow below steps

Go to python terminal :
>> python3
>> from application import app, db, Drink
      with app.app_context():
      db.create_all()
      db.session.add(Drink(name="cherry", description="tastes like ice cream"))
      db.session.commit()
      Drink.query.all()
>>
Note: The indentation in step 5




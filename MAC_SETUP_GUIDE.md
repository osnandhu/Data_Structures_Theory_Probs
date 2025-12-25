# MacBook Setup Guide - Start in 10 Minutes

**For**: Complete beginners on Mac
**Time**: 10-15 minutes
**Goal**: Get everything ready to start coding

---

## Step 1: Open Terminal (1 minute)

**Method 1** (Easiest):
1. Press `Cmd + Space` (this opens Spotlight)
2. Type: `terminal`
3. Press `Enter`

**Method 2**:
1. Open Finder
2. Go to Applications → Utilities
3. Double-click Terminal

You should see a window with text like:
```
Last login: Wed Dec 25 ...
username@MacBook ~ %
```

**Keep this window open!** You'll use it for everything.

---

## Step 2: Check if Python is Installed (1 minute)

In Terminal, type (then press Enter):
```bash
python3 --version
```

**What you might see:**

### ✅ Good: Shows Python version
```
Python 3.11.7
```
or
```
Python 3.12.0
```

**Action**: Nothing! You're ready. Skip to Step 3.

### ❌ Not installed: Shows error
```
command not found: python3
```

**Action**: Install Python from https://www.python.org/downloads/
- Click "Download Python 3.12.x"
- Open the downloaded file
- Follow installer (just keep clicking "Continue" and "Install")
- After install, close and reopen Terminal
- Try `python3 --version` again

---

## Step 3: Install Git (if not already installed) (2 minutes)

Check if you have Git:
```bash
git --version
```

**If you see a version number**: ✅ You're good!

**If you see error**: Install Git
```bash
# This will prompt you to install Command Line Tools
git --version
# Click "Install" when prompted
# Wait 5-10 minutes for installation
```

---

## Step 4: Clone Your Learning Repo (2 minutes)

```bash
# Go to your home directory
cd ~

# Clone the repo (DO NOT change this URL - it's the current repo)
# If repo is already local, skip to next command
git clone https://github.com/osnandhu/Data_Structures_Theory_Probs.git

# OR if you already have it, pull latest changes
cd Data_Structures_Theory_Probs
git pull

# Navigate into the folder
cd Data_Structures_Theory_Probs

# See what's inside
ls
```

You should see folders like:
```
00_Python_Crash_Course
01_Beginner
02_Intermediate
...
```

---

## Step 5: Choose Your Code Editor (5 minutes)

You need a way to edit code. Pick ONE:

### Option 1: VS Code (RECOMMENDED for beginners)

**Install**:
1. Go to: https://code.visualstudio.com/
2. Click "Download for macOS"
3. Open the downloaded file
4. Drag VS Code to Applications folder
5. Open VS Code

**Open your project in VS Code**:
```bash
# In Terminal, from your repo folder:
code .
```

This opens VS Code with your entire project!

**Install Python extension**:
- Click Extensions icon (left sidebar, 4 squares)
- Search "Python"
- Click "Install" on the Microsoft Python extension

### Option 2: nano (Built-in, no install needed)

Already installed! To edit a file:
```bash
nano filename.py
```

**Commands**:
- Type your code
- `Ctrl + O` (save)
- `Ctrl + X` (exit)

### Option 3: vim (Advanced, built-in)

Only if you know vim. Otherwise use VS Code or nano.

---

## Step 6: Test Your Setup (3 minutes)

### Create a test file:

**Using VS Code**:
1. Open VS Code in your repo folder
2. Right-click in file explorer → New File
3. Name it: `test.py`
4. Type:
```python
print("Hello from Mac!")
print("Python is working!")
```
5. Save (Cmd + S)

**Using nano**:
```bash
cd ~/Data_Structures_Theory_Probs
nano test.py
# Type the code above
# Ctrl + O, Enter (save)
# Ctrl + X (exit)
```

### Run your first Python program:
```bash
python3 test.py
```

**Expected output**:
```
Hello from Mac!
Python is working!
```

**If you see this**: ✅ YOU'RE READY TO CODE!

---

## Step 7: Run the Skills Assessment (5 minutes)

```bash
cd ~/Data_Structures_Theory_Probs/00_Python_Crash_Course
python3 assessment.py
```

You'll see questions. Now **edit the file** to answer them:

**Using VS Code**:
```bash
code assessment.py
```

**Using nano**:
```bash
nano assessment.py
```

**Uncomment your answers** (remove the `#` before your choice):
```python
# Before:
# background = "Never coded anything before"
# background = "Tried coding once or twice"

# After (uncomment YOUR answer):
background = "Never coded anything before"  # ← Removed the #
```

**Save and run**:
```bash
python3 assessment.py
```

Copy ALL the output and show it to me!

---

## Useful Mac Terminal Commands

```bash
# See where you are
pwd

# List files in current folder
ls

# Go to home directory
cd ~

# Go into a folder
cd folder_name

# Go up one folder
cd ..

# Clear screen
clear

# Copy text from Terminal
# Just select text and Cmd+C

# Paste in Terminal
Cmd + V
```

---

## Quick Troubleshooting

### "Permission denied" errors
Add `sudo` before the command:
```bash
sudo python3 ...
# It will ask for your Mac password
```

### "Command not found"
- Make sure you typed it correctly
- Make sure Python is installed: `python3 --version`
- Restart Terminal

### "No such file or directory"
- Check you're in the right folder: `pwd`
- List files to see what's there: `ls`
- Navigate to correct folder: `cd ~/Data_Structures_Theory_Probs`

### Python runs but code doesn't work
- Check for typos
- Make sure indentation is correct (Python cares about spaces!)
- Check error message - it usually tells you what's wrong

---

## Editor Shortcuts (VS Code)

```
Cmd + S          Save
Cmd + N          New file
Cmd + F          Find
Cmd + /          Comment/uncomment line
Cmd + `          Open terminal inside VS Code
Cmd + P          Quick file search
```

---

## You're Ready! 🎉

Now go to:
```bash
cd ~/Data_Structures_Theory_Probs
cat ROADMAP_30_DAYS_CRASH.md
```

Read your 30-day plan, then:
```bash
cd 00_Python_Crash_Course
cat Day1_Basics.md
```

**Start learning!**

---

## What to Do RIGHT NOW

1. ✅ Open Terminal
2. ✅ Check Python: `python3 --version`
3. ✅ Navigate to repo: `cd ~/Data_Structures_Theory_Probs`
4. ✅ Open in VS Code: `code .` (or use nano)
5. ✅ Run assessment: `cd 00_Python_Crash_Course && python3 assessment.py`
6. ✅ Edit assessment.py with your answers
7. ✅ Show me the output!

**Then we'll create your personalized 30-day schedule.**

Let's go! 🚀

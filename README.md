# RoomScanPlugin

A quick template for a room scanning plugin, useful if you have a Neocities site for a DOORS game.

## Requirements

Before starting, make sure you have:

* A Roblox Studio game
* A Neocities site
* Python installed on your computer
* A progress bar on your website
* A progress section on your website

## How to use

### 1. Set up Python

1. Open `ProgressServer.py`.
2. Find the Neocities username.
3. Change it to your Neocities username.

   * This is the part before `.neocities.org`.
4. Change the Neocities password to your Neocities password.
5. **Do not upload your modified Python file to GitHub if it contains your password.**
6. Save the file.

### 2. Start the Python server

1. Open the folder containing `ProgressServer.py`.
2. Click the address bar at the top of File Explorer.
3. Type:

```text
cmd
```

4. Press **Enter**.
5. Command Prompt should open in the folder containing the Python script.
6. Type:

```cmd
python ProgressServer.py
```

7. Press **Enter**.

If `python` doesn't work, try:

```cmd
py ProgressServer.py
```

You should see something similar to:

```text
SERVER STARTED
Listening on 127.0.0.1:8000
```

**Keep this Command Prompt window open while using the plugin.**

If you close it, the Roblox plugin will not be able to send the progress data to Python.

### 3. Set up the Roblox plugin

1. Open `RoomsProgress.lua`.
2. Find the total number of rooms.
3. Change it to the total number of rooms in your game.

For example:

```lua
total = 100
```

would mean your game has 100 rooms.

4. Save the plugin.
5. Open your game in Roblox Studio.
6. Go to **Home → Game Settings → Security**.
7. Make sure **Allow HTTP Requests** is enabled.
8. Open the **Plugins** tab.
9. Click **Scan Rooms**.

The plugin will scan your game for room signs and send the progress to the Python server.

### 4. Set up the website

1. Upload `progress.js` to your Neocities site.
2. Make sure your progress text uses the `room-progress` class:

```html
<p><strong class="room-progress">Loading progress...</strong></p>
```

3. Make sure your progress bar uses the `progress-fill` class:

```html
<div class="progress-bar">
    <div class="progress-fill"></div>
</div>
```

4. Add `progress.js` to your page:

```html
<script src="/progress.js"></script>
```

## What this adds

* A **Scan Rooms** button in the Roblox Studio Plugins tab
* Automatic room progress tracking
* Automatic percentage calculation
* Automatic progress bar updates
* Automatic progress text updates
* Automatic `progress.json` updates on your Neocities site

## How it works

```text
Roblox Studio
      ↓
RoomScanPlugin.lua
      ↓
Python Server
      ↓
progress.json
      ↓
Neocities
      ↓
Your Website
```

## Important

The Python server runs **locally on your computer**.

You must have the Python server running before clicking **Scan Rooms** in Roblox Studio.

The server uses:

```text
127.0.0.1:8000
```

Do not change the port unless you also change it in the Roblox plugin.

## Troubleshooting

### "Failed to send to Python"

Make sure:

* The Python server is running.
* The Command Prompt window is still open.
* The server says `Listening on 127.0.0.1:8000`.
* **Allow HTTP Requests** is enabled in Roblox Studio.
* The Roblox plugin is using the correct server address.

### The progress text updates but the bar doesn't

Make sure your progress bar contains:

```html
<div class="progress-fill"></div>
```

Also make sure your CSS does **not** force the width with:

```css
width: 4% !important;
```

I made that mistake.

The JavaScript needs to control the width.

### The website says "Progress unavailable"

Make sure:

* `progress.json` exists on your Neocities site.
* `progress.js` is loaded by your page.
* The Python server successfully uploaded `progress.json`.
* Your internet connection is working.

### Python says it cannot be found

Try:

```cmd
py ProgressServer.py
```

If that also fails, Python may not be installed or may not be added to your system PATH.

## Room numbering

The plugin looks for room signs formatted like:

```text
B-0001
B-0002
B-0003
```

and so on.

The starting room is excluded from the progress count, so the plugin subtracts one from the highest room number it finds.

For example:

```text
Highest room: B-0041
Completed rooms: 40
Progress: 4.0%
```

The percentage is calculated using:

```text
completed rooms ÷ total rooms × 100
```

## Files

* `RoomsProgress.lua` — Roblox Studio room scanner plugin
* `ProgressServer.py` — Local server that receives and uploads progress
* `progress.js` — Updates the website's progress text and bar

<!-- ## License

[Add your license here] -->

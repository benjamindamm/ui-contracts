# BrowserOS neo test sequence

Run scripts in numeric order against the freshly prepared/served host, in one owned BrowserOS tab.
They rederive page handles by exact URL and refs from snapshots; edit only the explicit loopback URL if using another port.
Browser actions use the SDK. `evaluate` provides asynchronous provider fixtures, source-bound model controls and raw measurement capture, never a fake keyboard/DOM event.
The server rejects duplicate case names. Use a new run directory for a repeat.

# ROBO iOS — Windows EXE starter project

This is a compact dark glass-style desktop UI demo with blue controls and animated particles. It is a starter interface, not a game cheat. Toggles are visual/demo only.

## Easiest way to build the EXE without installing anything on your PC

1. Create a new **public** GitHub repository (or use a private repository if your GitHub plan supports the needed Actions minutes).
2. Upload all files from this project ZIP to the repository. Make sure `.github/workflows/build-exe.yml` stays at that exact path.
3. Open the repository's **Actions** tab.
4. Select **Build ROBO iOS Windows EXE** and click **Run workflow**. If it does not appear, make a commit/push to `main` or `master`.
5. Wait until the workflow finishes with a green check.
6. Open the finished workflow run, scroll to **Artifacts**, and download **ROBO_iOS-Windows-EXE**.
7. Extract the downloaded ZIP. It contains `ROBO_iOS.exe`.

You do not need to install Python, write commands, or create a batch file on your computer. GitHub builds the EXE on a Windows runner.

## Demo login

Demo login: username `shafayy`, password `1`. This is local demo authentication, not production-grade security; connect a secure backend before using real accounts or subscriptions.

## Notes

- The Windows EXE is created by GitHub Actions, not included in this source ZIP.
- The first build may take a few minutes.
- The app uses a dark opaque base with animated blue particles; native Tkinter does not provide a true frosted-glass transparent window across all Windows versions.
- The feature controls are UI demonstrations only. No gameplay manipulation or anti-cheat bypass is implemented.

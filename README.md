# Remote Repositories

This repository is for providing feedback on the **Remote Repositories** extension. You can use the repository to report issues or submit feature requests.

The **Remote Repositories extension** lets you quickly browse, search, edit, and commit to any remote GitHub repository directly from within Visual Studio Code, with support for Azure repos coming soon.

## Why Remote Repositories?

As developers, we often clone Git repos locally just to browse them or make small edits. We may want to look at the source code of a library we use, experiment with new tools, or just feel the desire to learn something new. 

However, cloning repos takes time and maintenance, as your local copy can quickly become out of date if you don't pull changes regularly. Plus, if you don't know the codebase you're cloning, there may be security risks involved too!

The Remote Repositories extension in VS Code gives you a fast, convenient, and safe way to open, browse, and edit repos quickly.

Here are some **great situations** in which you may choose to use Remote Repositories to work on a codebase:

- To **browse**, **learn**, or **search** a codebase or parts of one, either as it exists today or at any point in history, directly in VS Code.
- To make **edits/tweaks** that don't require full validation, like building and running tests (validation can still happen in GitHub Actions triggered by a commit). This includes updates to docs or readme files, fixing typos, or make other smaller changes.
- To quickly review a **pull request** (PR), without having to check-out or in any way affect your local setup.
- To work on docs using VS Code's powerful **Markdown** editor, such as taking notes, or creating/editing/reviewing blog posts.
... And many more!

## Features

You can quickly and easily open a GitHub repository either by searching for **Remote Repositories: Open Remote Repository...** from the Command Palette (press `F1`), or choosing **Open Remote Repository...** from the remote indicator (the green button in the lower left corner of the status bar).

- Open any GitHub repository directly from GitHub — no cloning or local repository required
- Quickly search for a repository or pull request to open — can also copy/paste links directly from GitHub
- Repositories are always opened to the latest version on GitHub, unless you have uncommitted changes
- Similar to editing directly on GitHub, committing changes will go directly to GitHub — no pushing or publishing branches required
- Working changes are independent to the branch — allows working on multiple branches simultaneously!
     - When you pause work on one branch and switch to another one, you don’t need to stash your changes — they’ll stay on the previous branch, and when you go back, your changes will be there to pick up right where you left off
- Automatically detects if there are new changes on GitHub
     - An indicator of the number of unpulled commits will be shown in the status bar
     - Files with potential merge conflicts (e.g. you've modified the same file as someone else) will be highlighted
- Options to continue working in a more powerful environment
     - When you use **Continue Working on...** from the Command Palette or from the remote indicator, you're presented the option to continue your work locally, in a container volume (if you have the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension), or in GitHub Codespaces

## Releases

While an optional install, this extension releases along with VS Code. The [VS Code release notes](https://code.visualstudio.com/updates/) will include a summary of changes.

## Providing Feedback

You can use this repository to:

- Up-vote a feature request or request a new one
- Search for existing issues already reported for potential workarounds
- Report a problem if you don't find what you are looking for

If you have a question, connect with the community using any of these social platforms:

[![Twitter](docs/Twitter_Social_Icon_24x24.png)](https://twitter.com/code) [![Stack Overflow](docs/so-image-24x24.png)](https://stackoverflow.com/questions/tagged/vscode) [![VS Code Dev Community Slack](docs/Slack_Mark-24x24.png)](https://aka.ms/vscode-dev-community) [![VS CodeGitter](docs/gitter-icon-24x24.png)](https://gitter.im/Microsoft/vscode)

## License

By downloading and using the Remote Repositories extension and its related components, you agree to the product [license terms](https://marketplace.visualstudio.com/items/GitHub.remotehub/license) and [privacy statement](https://www.microsoft.com/en-us/privacystatement/EnterpriseDev/default.aspx).

License for this repository:

Copyright © Microsoft Corporation All rights reserved. 
Creative Commons Attribution 4.0 License (International): https://creativecommons.org/licenses/by/4.0/legalcode. 
For any code or snippets within this repository itself: https://github.com/microsoft/vscode-remote-repositories-github/blob/main/LICENSE-CODE. 

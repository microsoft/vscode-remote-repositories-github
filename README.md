cbowREADME.md

# Remote Repositories

This repository is for providing feedback on the **GitHub Repositories** and **Azure Repos** extensions. You can use the repository to report issues or submit feature requests.

The **GitHub Repositories extension** lets you quickly browse, search, edit, and commit to any remote GitHub repository directly from within Visual Studio Code. The **Azure Repos extension** lets you quickly browse, search, edit, and commit to any remote Azure Repos (part of Azure DevOps) repository directly from within Visual Studio Code.

## Why Remote Repositories?

As developers, we often clone Git repos locally just to browse them or make small edits. We may want to look at the source code of a library we use, experiment with new tools, or just feel the desire to learn something new.

However, cloning repos takes time and maintenance, as your local copy can quickly become out of date if you don't pull changes regularly. Plus, if you don't know the codebase you're cloning, there may be security risks involved too!

The GitHub Repositories and Azure Repos extensions in VS Code give you a fast, convenient, and safe way to open, browse, and edit repos quickly.

Here are some **great situations** in which you may choose to use GitHub Repositories or Azure Repos to work on a codebase:

- To **browse**, **learn**, or **search** a codebase or parts of one, either as it exists today or at any point in history, directly in VS Code.
- To **create, edit, and review** documentation, blog posts, notes, etc., using VS Code's powerful **Markdown** editor.
- To make **changes** that don't require building or running tests, although validations can still run in GitHub Actions or Azure Pipelines triggered on commit.
- To quickly review **pull requests** (PRs), without having to check-out or in any way affect your local setup.
... And many more!

## Features

This extension provides the following support for GitHub and Azure Repos repositories:

- **Open any GitHub or Azure Repos repository** directly from GitHub and Azure Repos &mdash; no cloning or local repository required.
- **Quickly search** for a repository or pull request to open &mdash; can also copy/paste links directly from GitHub or Azure Repos.
- Repositories always **open to the latest version** on GitHub or Azure Repos, unless you have uncommitted changes
- Similar to editing directly on GitHub or Azure Repos, **changes will go directly to GitHub or Azure Repos on commit** &mdash; no pushing or publishing branches required.
- Working changes are independent to the branch &mdash; **work on multiple branches simultaneously**!
  - When you pause work on one branch and switch to another one, you don’t need to stash your changes &mdash; they’ll stay on the previous branch, and when you go back, your changes will be there to pick up right where you left off.
- Automatically detects if there are new changes on GitHub or Azure Repos &mdash; always **stay up to date**.
  - Indicates the number of unpulled commits on the status bar.
  - **Flags potential merge conflicts** if you've modified the same file as someone else.
- Open Remote Repositories in the **Remote Explorer** to see all the repositories you've accessed.
  - You can quickly open a remote repository to continue working, or view and compare any uncommitted changes you may have. Additionally, you can **apply uncommitted changes across branches** from the same repository.
- Search files in the repository.

## Integration with vscode.dev

**GitHub Repositories** and **Azure Repos** are built into vscode.dev so that you can easily use them right from your browser.

You can use the GitHub Repositories and Azure Repos extensions directly in your browser in the following ways:
- Prefix any GitHub or Azure Repos repository URL with `https://vscode.dev`, or
- Visit https://vscode.dev and select `Open Remote Repository`, or
- On GitHub and Azure DevOps, just press `.`

GitHub Repositories URLs have the following structure:

```
https://vscode.dev/github/<owner>/<repo>
```

Azure Repos URLs have the following structure:

```
https://vscode.dev/azurerepos/<organization>/<project>/<repo>
```

### Continue Working On...

When working with either GitHub or Azure repositories, you have several options to continue working in a more powerful environment.

- When you choose _Continue Working On..._ from the Command Palette or from the remote indicator, you're presented the option to continue your work locally, in a container volume (if you have the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension), or in GitHub Codespaces.

  ![Continue On command options](https://raw.githubusercontent.com/microsoft/vscode-remote-repositories-github/main/docs/continue-on.png)


## Releases

While an optional install, this extension releases along with VS Code. The [VS Code release notes](https://code.visualstudio.com/updates/) will include a summary of changes.

You can also install the pre-release version of this extension for early feedback and testing. The pre-release version of this extension works best in VS Code Insiders. You can learn more about VS Code's support for pre-release extensions [here](https://code.visualstudio.com/api/working-with-extensions/publishing-extension#prerelease-extensions). 

The pre-release version of this extension replaces the [_GitHub Repositories (Insiders)_ extension](https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub-insiders), which is now deprecated. If you are still using the _GitHub Repositories (Insiders)_ extension and want to migrate to pre-releases,
1. Commit any uncommitted changes in your existing GitHub Repositories workspaces to retain access to them after you uninstall the extension.
2. Uninstall the _GitHub Repositories (Insiders)_ extension.
3. Install the pre-release edition of the GitHub Repositories extension.

## Providing Feedback

You can use this repository to:

- Up-vote a feature request or request a new one
- Search for existing issues already reported for potential workarounds
- Report a problem if you don't find what you are looking for

If you have a question, connect with the community using any of these social platforms:

[![Twitter](docs/Twitter_Social_Icon_24x24.png)](https://twitter.com/code) [![Stack Overflow](docs/so-image-24x24.png)](https://stackoverflow.com/questions/tagged/vscode) [![VS Code Dev Community Slack](docs/Slack_Mark-24x24.png)](https://aka.ms/vscode-dev-community) [![VS CodeGitter](docs/gitter-icon-24x24.png)](https://gitter.im/Microsoft/vscode)

## License

By downloading and using the GitHub Repositories extension and its related components, you agree to the product [license terms](https://marketplace.visualstudio.com/items/GitHub.remotehub/license) and [privacy statement](https://www.microsoft.com/en-us/privacystatement/EnterpriseDev/default.aspx).

License for this repository:

Copyright © Microsoft Corporation All rights reserved. 
Creative Commons Attribution 4.0 License (International): https://creativecommons.org/licenses/by/4.0/legalcode. 
For any code or snippets within this repository itself: https://github.com/microsoft/vscode-remote-repositories-github/blob/main/LICENSE-CODE. 

# 🕵️ Pinkerton
> Investigating JavaScripts files since 1850

<div align="center">
    <img src="./assets/preview.png">
</div>

<br>

<p align="center">
    <img src="https://img.shields.io/github/license/oppsec/Pinkerton?color=green&logo=github&style=for-the-badge">
    <img src="https://img.shields.io/github/issues/oppsec/Pinkerton?color=green&logo=github&style=for-the-badge">
    <img src="https://img.shields.io/github/stars/oppsec/pinkerton?color=green&logo=github&style=for-the-badge">
    <img src="https://img.shields.io/github/forks/oppsec/Pinkerton?color=green&logo=github&style=for-the-badge">
    <img src="https://img.shields.io/github/v/release/oppsec/pinkerton?color=green&logo=github&style=for-the-badge">
    <img src="https://img.shields.io/github/languages/code-size/oppsec/Pinkerton?color=green&logo=github&style=for-the-badge">
</p>

___

<br>

<p> ️🕵️ <b>Pinkerton</b> is a Python tool created to crawl JavaScript files and search for secrets </p>

<br>

## ⚡ Installing / Getting started

<p> A quick guide of how to install and use Pinkerton. </p>

```
1. Clone the repository with: git clone https://github.com/oppsec/pinkerton.git
2. Install the libraries with: pip3 install -r requirements.txt
3. Run Pinkerton with: python3 main.py -u https://example.com
```

<br>

### 🐳 Docker
If you want to use pinkerton in a Docker container, follow this commands:

```
1. Clone the repository - git clone https://github.com/oppsec/pinkerton.git
2. Build the image - sudo docker build -t pinkerton:latest .
3. Run container - sudo docker run pinkerton:latest
```

<br><br>

### ⚙️ Pre-requisites
- [Python 3](https://www.python.org/downloads/) installed on your machine.
- Install the libraries with `pip3 install -r requirements.txt`

<br><br>

### 🎥 Demo
[![asciicast](https://asciinema.org/a/7gybqzcDsIm0nkDhUhhI9JFRA.svg)](https://asciinema.org/a/7gybqzcDsIm0nkDhUhhI9JFRA)

<br><br>

### ✨ Features
- Works with ProxyChains
- Fast scan
- Low RAM and CPU usage
- Open-Source
- Python ❤️

<br><br>

### 📚 To-Do
- [x] Add more secrets regex pattern
- [ ] Improve JavaScript file extract function
- [ ] Improve pattern match system
- [ ] Add pass list file method

<br><br>

### 🔨 Contributing

A quick guide of how to contribute with the project.

```
1. Create a fork from Pinkerton repository
2. Clone the repository with git clone https://github.com/your/pinkerton.git
3. Type cd pinkerton/
4. Create a branch and make your changes
5. Commit and make a git push
6. Open a pull request
```

<br><br>

### 🙏 Credits
- [m4ll0k (SecretFinder creator)](https://github.com/m4ll0k) for the regex patterns
- [h33lit (Jubaer Alnazi)](https://github.com/h33tlit) for the regex patterns
- [zricethezav (GitLeaks creator)](https://github.com/zricethezav/gitleaks) for the regex patterns

<br><br>

### ⚠️ Warning
- The developer is not responsible for any malicious use of this tool.

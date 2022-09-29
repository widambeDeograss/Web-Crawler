<h1>
  <a href="http://196.192.78.28:8082/noberto/spiderweb.git">
    <!-- Please provide path to your logo here -->
    <img src="logo/Untitled_design-removebg-preview.png" alt="spiderWeblogo" width="120" height="120">
  </a>
<strong>Web Crawler</strong>
</h1>

<div align="center">
  <br />
  <a href="#about"><strong>Explore the screenshots »</strong></a>
  <br />
</div>

<div align="center">

[![Project license](https://img.shields.io/github/license/dec0dOS/spiderweb.svg?style=flat-square)](LICENSE)
[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/dec0dOS/spiderweb/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Project assistance](#project-assistance)
- [License](#license)

</details>



## About

<table><tr><td>
An information gathering platform that collects open source information from different sources on Internet and provide analyzed and meaningful query results.

<details>
<summary>Screenshots</summary>
<br>

|                               Home Page                               |                               Login Page                               |
| :-------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| <img src="docs/images/screenshot.png" title="Home Page" width="100%"> | <img src="docs/images/screenshot.png" title="Login Page" width="100%"> |

</details>

</td></tr></table>

### Built With

> <li>Python</li>
> <li>MongoDB</li>


## Getting Started

### Prerequisites

> Scrapy Framework<br />
> urllib <br />
> bs4 <br />
> Requests

### Installation

```
git clone http://196.192.78.28:8082/noberto/spiderweb.git 
```

<div style="margin:auto">OR</div> 

```
git clone git@196.192.78.28:noberto/spiderweb.git
```

## Usage

To start the crawling process, run the command:
```
scrapy crawl web -o <filename>.csv/json/jl/xml
```

<br>To scrap the title, description and keywords for all the crawled links:<br>

In the **PageContent** class change file reference to your url file.<br>
i.e.
>with open('updated2L.jl') as f:

Change the name 'updated2L.jl' into your urlfile name.<br><br>

Then run the following command:
```
scrapy crawl page_content -o <filename>.csv/json/jl/xml<br>
```

<br>To extract image links for all the crawled links:<br>

In the **ImageExtractor** class change file reference to your url file.<br>
i.e.
>with open('updated2L.jl') as f:

Change the name 'updated2L.jl' into your urlfile name.<br><br>

Then run the following command:
```
scrapy crawl image -o <filename>.csv/json/jl/xml<br>
```

<br>To extract pdf links and pdfs for all the crawled links:<br>

In the **PdfExtractor** class change file reference to your url file.<br>
i.e.
>with open('updated2L.jl') as f:

Change the name 'updated2L.jl' into your urlfile name.<br><br>

Then run the following command:
```
scrapy crawl pdf -o <filename>.csv/json/jl/xml<br>
```

<br>To extract bdy text for all the crawled links:<br>

In the **HtmlParser** class change file reference to your url file.<br>
i.e.
>with open('updated2L.jl') as f:

Change the name 'updated2L.jl' into your urlfile name.<br><br>

Then run the following command:
```
scrapy crawl body -o \<filename>.csv/json/jl/xml<br>
```

## Support


Together, we can make SpiderWeb **better**!

## License

This project is licensed under the 

See [LICENSE](LICENSE) for more information.


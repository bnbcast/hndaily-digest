# Daily Digest

A daily Hacker News digest generator and newspaper web app.

## Newspaper app

The React and Vite site is deployed at
https://bnbcast.github.io/hndaily-digest/.

To run it locally:

```powershell
npm ci
npm run dev
npm run build
```

The `deploy-pages.yml` workflow builds the app and deploys it to GitHub Pages.
Digest data is fetched from the `digest/` directory in this repository.

## Daily digest generator

`bot.py` fetches the five top Hacker News stories and writes a dated Markdown
file under `digest/YYYY/MM/`. The `daily.yml` workflow runs each day at 03:00
UTC and commits any new digest.
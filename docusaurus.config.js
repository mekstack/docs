import { themes as prismThemes } from "prism-react-renderer";

const path = require("path");

const config = {
  title: "Mekstack Docs",
  tagline:
    "Mekstack – опенсорсное гиперконвергентное высокодоступное облако для студентов МИЭМ",
  favicon: "img/favicon.ico",

  url: "https://docs.mekstack.ru/",
  baseUrl: "/",

  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      {
        docs: {
          routeBasePath: "/",
          sidebarPath: "./sidebars.js",
          editUrl: ({ docPath }) =>
            `https://github.com/mekstack/docs/edit/master/${docPath}`,
        },
        blog: false,
        theme: {
          customCss: [
            // './node_modules/modern-normalize/modern-normalize.css',
            "./src/css/custom.scss",
          ],
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      logo: {
        alt: "Mekstack Logo",
        src: "https://storage.yandexcloud.net/mekstack-static/mekstack-logo.svg",
      },
      items: [
        {
          href: "https://mekstack.ru",
          label: "Dashboard",
          position: "left",
        },
        {
          href: "https://vpnaas.mekstack.ru",
          label: "VPNaaS",
          position: "left",
        },
        {
          href: "https://chat.miem.hse.ru/#narrow/stream/2057",
          label: "Zulip Chat",
          position: "left",
        },
        {
          href: "https://github.com/mekstack/",
          label: "GitHub",
          position: "left",
        },
      ],
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  },

  plugins: ["docusaurus-plugin-sass"],
};

export default config;

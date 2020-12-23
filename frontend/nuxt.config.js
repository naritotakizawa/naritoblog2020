export default {
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'Top',
    titleTemplate: '%s | Blog.narito',
    htmlAttrs: {
      lang: 'ja',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: '取り留めのないブログ',
      },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
    { src: '~plugins/quill.js', ssr: false },
    '~/plugins/filter.js',
    { src: '~plugins/adobefonts.js', ssr: false },
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',

    '@nuxtjs/auth',

    '@nuxtjs/toast',
  ],

  // Axios module configuration (https://go.nuxtjs.dev/config-axios)
  axios: {
    baseURL: 'http://backend:8000/api',
    browserBaseURL: '/api',
  },

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {},

  auth: {
    redirect: {
      login: '/login', // 未ログイン時に認証ルートへアクセスした際のリダイレクトURL
      home: '/', // ログイン後のリダイレクトURL
      logout: false,
    },
    strategies: {
      local: {
        tokenType: 'JWT',
        endpoints: {
          login: {
            url: '/auth/jwt/create/',
            method: 'post',
            propertyName: 'access',
          },
          user: { url: '/auth/users/me/', method: 'get', propertyName: false },
        },
      },
    },
  },
  toast: {
    // 右上にtoastを表示
    position: 'bottom-right',
    // 特に指定しなくても5秒で消えるように設定
    duration: 3000,
  },
}

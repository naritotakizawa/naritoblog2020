<template>
  <div class="container">
    <p v-if="$fetchState.pending" class="loading-wrapper">
      <span class="loading"></span>
    </p>
    <p v-else-if="$fetchState.error">何かエラーが起きています。</p>
    <section v-else>
      <article v-for="post in posts.results" :key="post.id">
        <time>{{ post.created_at | date }}</time>

        <h2>
          <NuxtLink :to="{ name: 'posts-slug', params: { slug: post.slug } }">
            {{ post.title }}
          </NuxtLink>
        </h2>
        <p>{{ post.description }}</p>
      </article>

      <nav>
        <NuxtLink :to="getPreviousURL" v-if="posts.previous">
          Previous
        </NuxtLink>

        <span>{{ posts.currentPageNumber }} / {{ posts.totalPageNumber }}</span>

        <NuxtLink :to="getNextURL" v-if="posts.next"> Next </NuxtLink>
      </nav>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      posts: {},
    }
  },
  computed: {
    getPreviousURL() {
      let url = `?page=${this.posts.currentPageNumber - 1}`
      const keyword = this.$route.query.keyword
      if (keyword) {
        url += `&keyword=${keyword}`
      }
      return url
    },
    getNextURL() {
      let url = `?page=${this.posts.currentPageNumber + 1}`
      const keyword = this.$route.query.keyword
      if (keyword) {
        url += `&keyword=${keyword}`
      }
      return url
    },
  },
  activated() {
    if (this.$fetchState.timestamp <= Date.now() - 30000) {
      this.$fetch()
    }
  },
  watch: {
    '$route.query': '$fetch',
  },
  async fetch() {
    let url = '/posts/'

    const page = this.$route.query.page || 1
    url += `?page=${page}`

    const keyword = this.$route.query.keyword || ''
    url += `&keyword=${keyword}`

    url = encodeURI(url)
    this.posts = await this.$axios.$get(url)
  },

  methods: {},
}
</script>
<style scoped>
article {
  margin-bottom: 32px;
}

@media (min-width: 768px) {
  article {
    display: grid;
    grid-template-columns: 0.25fr 0.75fr;
    margin-bottom: 64px;
  }
}

article > time {
  font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier,
    monospace;
  grid-column: 1;
  grid-row: 1;
  color: #959da5;
  max-width: 266px;
}

article > h2 {
  grid-column: 2;
  grid-row: 1;
  font-size: 20px;
  max-width: 620px;
}

article > p {
  grid-column: 2;
  grid-row: 2;
  font-size: 16px;
  margin: 14px 0 16px 0;
  color: #586069;
  line-height: 1.75;
  max-width: 620px;
}

nav {
  text-align: center;
}

nav > * {
  display: inline-block;
  padding: 0 8px;
}
</style>

<template>
  <article class="min-container">
    <p v-if="$fetchState.pending" class="loading-wrapper">
      <span class="loading"></span>
    </p>
    <p v-else-if="$fetchState.error">何かエラーが起きています。</p>
    <img :src="post.image" :alt="post.title" />
    <header>
      <time>{{ post.created_at | date }}</time>
      <h1>{{ post.title }}</h1>
    </header>

    <p v-html="post.text" id="content"></p>

    <div v-if="auth.loggedIn" id="admin-menu">
      <NuxtLink
        class="button"
        :to="{ name: 'posts-update-slug', params: { slug: post.slug } }"
      >
        記事を更新する
      </NuxtLink>
      <button @click="isOpen = true">記事を削除する</button>
    </div>

    <transition name="zoom">
      <Dialog v-if="isOpen" @close="isOpen = false">
        <p class="dialog-text">削除します。よろしいですか？</p>
        <button type="button" @click="deletePost" class="dialog-button">
          はい
        </button>
        <button type="button" @click="isOpen = false" class="dialog-button">
          いいえ
        </button>
      </Dialog>
    </transition>
  </article>
</template>
<script>
export default {
  data() {
    return {
      post: {},
      isOpen: false,
    }
  },
  computed: {
    auth() {
      return this.$store.$auth
    },
  },
  async fetch() {
    this.post = await this.$axios.$get(`/posts/${this.$route.params.slug}/`)
  },
  methods: {
    goBack() {
      return this.$router.go(-1)
    },
    async deletePost() {
      await this.$axios.$delete(`/posts/${this.post.slug}/`)
      this.$toast.show('削除しました')
      this.$router.push('/')
    },
  },
  head() {
    return {
      title: this.post.title,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: this.post.description,
        },
      ],
    }
  },
}
</script>
<style scoped>
article > header {
  margin: 50px 0;
}
header > h1 {
  font-size: 20px;
}

@media (min-width: 768px) {
  header > h1 {
    font-size: 48px;
  }
}

header > time {
  font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier,
    monospace;
  color: #959da5;
}

#content {
  max-width: 640px;
}

#content >>> p {
  font-size: 16px;
  line-height: 1.75;
}

#content >>> a {
  color: #4083ff;
  text-decoration: underline;
}

#admin-menu {
  margin-top: 50px;
}

#admin-menu > * {
  margin-right: 30px;
}

.dialog-text {
  margin-bottom: 1em;
  font-size: 16px;
}

.dialog-button {
  margin-right: 12px;
}
</style>

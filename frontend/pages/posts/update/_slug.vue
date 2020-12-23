<template>
  <div class="min-container">
    <PostEditor
      @send="send"
      :post="post"
      v-if="!$fetchState.pending"
    ></PostEditor>
  </div>
</template>

<script>
export default {
  data() {
    return {
      post: null,
    }
  },
  middleware: ['auth'],
  methods: {
    async send(form) {
      const formData = new FormData()
      formData.append('title', form.title)
      formData.append('slug', form.slug)
      formData.append('description', form.description)
      if (form.image) {
        formData.append('image', form.image)
      }

      formData.append('text', form.text)
      const config = {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }
      await this.$axios
        .$patch(`/posts/${this.post.slug}/`, formData, config)
        .then((response) => {
          this.$router.push({
            name: 'posts-slug',
            params: { slug: response.slug },
          })
          this.$toast.show('更新しました')
        })
        .catch((error) => {
          if (error.response.status === 400) {
            for (const key in error.response.data) {
              for (const message of error.response.data[key]) {
                this.$toast.show(message)
              }
            }
          }
        })
    },
  },
  async fetch() {
    this.post = await this.$axios.$get(`/posts/${this.$route.params.slug}/`)
  },
}
</script>

<style scoped></style>

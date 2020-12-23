<template>
  <div class="min-container">
    <PostEditor @send="send"></PostEditor>
  </div>
</template>

<script>
export default {
  data() {
    return {}
  },
  middleware: ['auth'],
  methods: {
    async send(form) {
      const formData = new FormData()
      formData.append('title', form.title)
      formData.append('slug', form.slug)
      formData.append('image', form.image)
      formData.append('text', form.text)
      formData.append('description', form.description)
      const config = {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }
      await this.$axios
        .$post('/posts/', formData, config)
        .then((response) => {
          this.$router.push({
            name: 'posts-slug',
            params: { slug: response.slug },
          })
          this.$toast.show('保存しました')
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
}
</script>

<style scoped></style>

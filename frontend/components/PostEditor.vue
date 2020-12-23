<template>
  <div>
    <form @submit.prevent="onSubmit">
      <div class="field">
        <label for="title">タイトル</label>
        <input type="text" v-model="form.title" id="title" />
      </div>
      <div class="field">
        <label for="slug">URL</label>
        <input type="text" v-model="form.slug" id="slug" />
      </div>
      <div class="field">
        <label for="image">サムネイル</label>
        <input type="file" @change="onSumbnailUpload" id="image" />
        <p v-if="form.imageURL">
          現在の画像: <a :href="form.imageURL">{{ form.imageURL }}</a>
        </p>
      </div>
      <div class="field">
        <label for="description">概要</label>
        <textarea v-model="form.description" id="description"></textarea>
      </div>

      <div class="field">
        <label>本文</label>
        <client-only placeholder="エディタのロード中">
          <vue-editor
            id="editor"
            :useCustomImageHandler="true"
            @image-added="handleImageAdded"
            v-model="form.text"
          >
          </vue-editor>
        </client-only>
      </div>

      <button type="submit">送信する</button>
    </form>
  </div>
</template>

<script>
export default {
  props: ['post'],
  data() {
    return {
      form: {
        title: '',
        slug: '',
        text: '',
        image: null,
        description: '',
        imageURL: '',
      },
    }
  },
  created() {
    if (this.post) {
      this.form.title = this.post.title
      this.form.slug = this.post.slug
      this.form.text = this.post.text
      this.form.description = this.post.description
      this.form.imageURL = this.post.image
    }
  },
  methods: {
    async handleImageAdded(file, Editor, cursorLocation, resetUploader) {
      const formData = new FormData()
      formData.append('image', file)
      const response = await this.$axios.$post('/upload/', formData)
      const url = response.url
      Editor.insertEmbed(cursorLocation, 'image', url)
      resetUploader()
    },
    onSumbnailUpload(event) {
      this.form.image = event.target.files[0]
    },
    onSubmit(event) {
      let isInputOk = true
      if (!this.form.title) {
        this.$toast.show('タイトルがありません。')
        isInputOk = false
      }
      if (!this.form.slug) {
        this.$toast.show('URLがありません。')
        isInputOk = false
      }
      if (!this.form.text) {
        this.$toast.show('本文がありません。')
        isInputOk = false
      }
      if (!this.form.image && !this.form.imageURL) {
        this.$toast.show('サムネイルがありません。')
        isInputOk = false
      }
      if (isInputOk) {
        this.$emit('send', this.form)
      }
    },
  },
}
</script>

<style scoped>
a {
  color: #4083ff;
  text-decoration: underline;
}
</style>

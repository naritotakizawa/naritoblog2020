<template>
  <form class="min-container" @submit.prevent="login">
    <div class="field">
      <label for="username">ユーザーネーム</label>
      <input id="username" v-model="form.username" type="text" />
    </div>
    <div class="field">
      <label for="password">パスワード</label>
      <input id="password" v-model="form.password" type="password" />
    </div>
    <button type="submit">送信</button>
  </form>
</template>

<script>
export default {
  middleware({ store, redirect }) {
    if (store.$auth.loggedIn) {
      redirect('/')
    }
  },
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
    }
  },
  methods: {
    async login() {
      const response = await this.$auth
        .loginWith('local', { data: this.form })
        .catch((err) => {
          return err.response
        })

      if (response.status === 200) {
        this.$toast.show('ログインしました')
      } else {
        this.$toast.show('ログインに失敗しました')
      }
    },
  },
}
</script>

<style scoped></style>

<template>
  <header>
    <NuxtLink id="left" :to="{ name: 'index' }"> Blog.narito </NuxtLink>

    <div id="right">
      <ul>
        <li>
          <a hfef @click.prevent="isOpen = true"> Search </a>
        </li>

        <li v-if="auth.loggedIn">
          <NuxtLink :to="{ name: 'posts-new' }"> Add </NuxtLink>
        </li>

        <li v-if="auth.loggedIn">
          <a v-if="auth.loggedIn" href="#" @click.prevent="logout"> Logout </a>
        </li>

        <li v-else>
          <NuxtLink :to="{ name: 'login' }"> Login </NuxtLink>
        </li>
      </ul>
    </div>

    <transition name="zoom">
      <Dialog v-if="isOpen" @close="isOpen = false">
        <form @submit.prevent="search">
          <div class="field">
            <input v-model="keyword" type="text" />
          </div>
          <button type="submit" class="search-button">検索する</button>
        </form>
      </Dialog>
    </transition>
  </header>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false,
      keyword: '',
    }
  },
  computed: {
    auth() {
      return this.$store.$auth
    },
  },
  methods: {
    logout() {
      this.$auth.logout()
      this.$toast.show('ログアウトしました')
    },
    search() {
      this.$router.push({
        name: 'index',
        query: { keyword: this.keyword },
      })
      this.isOpen = false
    },
  },
}
</script>
<style scoped>
header {
  margin-top: 10px;
  margin-bottom: 64px;
}

@media (min-width: 768px) {
  header {
    height: 200px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    align-items: center;
    margin-top: 0;
    margin-bottom: 50px;
  }
}

header > * {
  grid-row: 1;
}

#left {
  grid-column: 1;
  justify-self: start;
  font-size: 40px;
  letter-spacing: 2px;
  font-weight: bold;
}

#right {
  grid-column: 2;
  justify-self: end;
}

ul {
  list-style-type: none;
}

li {
  display: inline-block;
  margin-right: 10px;
}
</style>

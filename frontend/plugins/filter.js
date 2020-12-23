import Vue from 'vue'

Vue.filter('date', value => {
    const date = new Date(value);
    return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
})
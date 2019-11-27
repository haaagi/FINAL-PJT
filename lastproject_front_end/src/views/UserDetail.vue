<template>
  <div class="user-detail">
    <h1>로그인됨</h1>
    <div>{{ getuserinfo.age }}</div>
    <div>{{ getuserinfo.username }}</div>
    <button>팔로우</button>

  </div>
</template>

<script>
  import {
    mapGetters
  } from 'vuex';
  export default {
    name: 'UserDetail',
    computed: {
      ...mapGetters(['getuserinfo'])
    }
  }
</script>

<style>
</style>
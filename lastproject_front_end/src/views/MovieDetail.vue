<template>
  <div class="moviedetail">
      <router-view />
 <h3> {{ getmovieOne.title }} </h3>
  </div>
</template>

<script>
  import {
    mapGetters
  } from 'vuex';
  export default {
    name: 'MovieDetail',
    computed: {
      ...mapGetters(['getmovieOne'])
    }
  }
</script>

<style>

</style>
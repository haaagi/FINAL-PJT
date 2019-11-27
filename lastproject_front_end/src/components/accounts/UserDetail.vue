<template>
  <div>
      <div>{{ getuserinfo.age }}</div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
    name:'UserDetail',
    computed: {
        ...mapGetters(['getuserinfo'])
    }
}
</script>

<style>
</style>
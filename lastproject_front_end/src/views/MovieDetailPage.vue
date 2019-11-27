<template>
  <div class="movie-detail-page">
    <MovieDetail :movie="movie" />

    
    <router-view/>
    

  </div>
</template>


<script>
import router from '../router';

export default {
  name: 'home',
  components: {
  },
  data () {
    return {
      selecte_id: 0,
      movieOne: [],
    }
  },
  mounted () {
      router.push("/moviedetailpage");
    },

}

</script>

<style>
</style>
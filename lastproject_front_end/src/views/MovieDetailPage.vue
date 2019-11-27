<template>
  <div class="movie-detail-page">
    <MovieDetail :movie="movie" />

    
    <router-view/>
    

  </div>
</template>


<script>
import {
  mapGetters
} from 'vuex'


export default {

  name: 'MovieDetailPage',
  components: {
  },
  computed: {
    ...mapGetters(['getmovieOne'])
  }


}

</script>


<style>
</style>
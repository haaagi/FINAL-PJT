<template>
  <div class="movie-detail-page">

    <router-view>
    <MovieDetailPage :movie="movie"/>
    </router-view>
  </div>
</template>


<script>
import MovieDetail from'../components/movies/MovieDetail';
import router from '../router';

export default {
  name: 'home',
  components: {
    // MovieDetail,
  },
  data () {
    return {
      movie: Object,
    }
  },
  mounted () {
      router.push("/moviedetail");
    },

}

</script>

<style>
</style>
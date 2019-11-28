<template>
  <div>
    <button @click="recommend()">추천영화 보가
    </button>
    <div v-for="movie in new_movies" :key="movie.id">
        <img :src="movie.poster_url" :alt="movie.title">
    </div>
      
      
  </div>
</template>

<script>
export default {
    name:'RecommendMovie',
    data () {
        return {
            new_movies: [],
        }
    },
    computed: {
        
    },
    props: {
        movies: Array,
        getuserinfo: Array,
    },
    methods: {
        recommend () {
            for (var i=0; i<this.getuserinfo.stars.length; i++) {
                for (var j=0; j<this.movies.length; j++) {
                    for (var x =0; x <this.movies[j].like_users.length; x++) {
                        if(this.movies[j].like_users[x] === this.getuserinfo.start[i]) {
                            this.new_movies.push(this.movies[j])
                        }
                    }
                }
            }
        }  
    }
    // filterMovies() {
    //     if (this.selectedGenre === '전체보기') {
    //       return this.movies;
    //     } else {
    //       return this.movies.filter(movie => movie.genre1 === this.selectedGenre || movie.genre3 === this
    //         .selectedGenre);
    //     }
    //   }
}
</script>

<style>

</style>
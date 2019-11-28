<template>
  <div>
    <button @click="recommend()">추천영화 보가
    </button>
    <div class="row">
        <div v-for="movie in n_movies" :key="movie.id">
            <img :src="movie.poster_url" :alt="movie.title">
        </div>
    </div>
    
      
      
  </div>
</template>

<script>
import {
    mapGetters
  } from 'vuex';
export default {
    name:'RecommendMovie',
    data () {
        return {
            new_movies: [],
            temp: [],
            n_movies:[],
        }
    },
    props: {
        movies: Array,
    },
    computed: {
        ...mapGetters(['getuserinfo'])
    },
    methods: {
        recommend () {
            for (var key in this.getuserinfo) {
                if (key === 'stars') {
                    this.temp = this.getuserinfo[key]
                }
                for (var i in this.temp) {
                    for (var k in this.movies) {
                        for (var j in this.movies[k]['like_users']) {
                            if (this.temp[i] === this.movies[k]['like_users'][j]) {
                                this.new_movies.push(this.movies[k])
                            }
                        }
                    }
                }
            }
            this.n_movies = new Set(this.new_movies)
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
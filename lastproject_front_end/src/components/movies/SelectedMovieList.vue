<template>
    <div>
        <img :src="movie.poster_url" :alt="movie.title">
        <p>{{ movie.title }}</p>
    </div>
</template>

<script>
export default {
    name: 'SelectedMovieList',
    props:{
        movie: Object,
    }
}
</script>

<style>

</style>
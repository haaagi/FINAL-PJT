const axios = require('axios');



const state = {
    movieOne: []
};


const getters = {
    getmovieOne: state => state.movieOne
};

const mutations = {
    setmovieOne: (state, one) => state.movieOne = one
};

const actions = {
    
}
export default {
    state, getters, mutations, actions
}

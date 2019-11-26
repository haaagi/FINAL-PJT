const state = {
    token: null,
};

const getters = {
    isLoggedIn: (state) => {
        if (state.token === null) {
            return false;
        } else {
            return true;
        }
    }
};

const mutations = {
    setToken: (state, token) => state.token = token,
};

const actions = {
    logout: ({commit}) => {
        commit('setToken', null)
    },
    login: ({ commit }, token) => {
        commit('setToken', token)
    },
};

export default {
    state, getters, mutations, actions
}
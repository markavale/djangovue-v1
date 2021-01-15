import { axiosBase } from "@/api/axiosConfig";


const state = {
    mail: {},
    rating: {},
    skipper: {}
}

const getters = {

}

const actions = {
    sendMail: (context, payload) => {
        return new Promise((resolve, reject) => {
            axiosBase
                .post('api/messages/', payload)
                .then((res) => {
                    resolve(true);
                    context.commit('newMail', res.data);
                })
                .catch((err) => reject(err));
        })
    },
    addRating: (context, payload) => {
        return new Promise((resolve, reject) => {
            axiosBase
                .post('api/ratings/', payload)
                .then(res => {
                    resolve(true);
                    context.commit('newRating', res.data);
                })
                .catch(err => reject(err));
        })
    },
    skipUser: (context, payload) => {
        return new Promise((resolve, reject) => {
            axiosBase
                .post('api/skipper/', payload)
                .then(res => {
                    resolve(true);
                    context.commit('newSkipper', res.data);
                })
                .catch(err => reject(err));
        })
    }
}
const mutations = {
    newMail: (state, newMail) => state.mail.unshift(newMail),
    newRating: (state, newRating) => state.rating.unshift(newRating),
    newSkipper: (state, newSkipper) => state.skipper.unshift(newSkipper),
}


export default {
    state,
    getters,
    actions,
    mutations,
}
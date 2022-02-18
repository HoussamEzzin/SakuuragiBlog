import store from 'store';

export const set = (key,value)=> {
    store.set(key,value)
}

export const get = (key) => {
    return store.get(key)
}

export const remove = (key) => {
    store.remove(key)
}

export const clear = () => {
    store.clearAll()
}
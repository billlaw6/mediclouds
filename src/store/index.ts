import { combineReducers, createStore } from 'redux';
import { countReducer } from './reducers';

const rootReducer = combineReducers({
    count: countReducer,
});

export type AppState = ReturnType<typeof rootReducer>;

export default function configureStore() {
    const store = createStore(rootReducer);
    return store;
}

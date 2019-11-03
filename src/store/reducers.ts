import { ADD_COUNT, IAddCountAction } from './types';

export function countReducer(state = 0, action: IAddCountAction) {
    switch (action.type) {
        case ADD_COUNT:
            return state + 1;
        default:
            return state;
    }
}

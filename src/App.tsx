import React from 'react';
import { connect } from 'react-redux';
import { AppState } from './store';
import { addCount } from './store/actions';
import './App.css';

// 定义本Component创建时需要的参数类型
interface IAppProps {
    count: number;
    addCount: typeof addCount;
}

class App extends React.Component<IAppProps, {}> {
    render() {
        const { count } = this.props;
        return (
            <div className="App">
                <span>{count}</span>
                <button onClick={this.handleClick}>+</button>
            </div>
        );
    }

    private handleClick = () => {
        this.props.addCount();
    };
}

// 从state里摘出本Component需要的部分作为本Component构建的参数
// state初始值在reducers里定义了
const mapStateToProps = (state: AppState) => ({
    count: state.count,
});

// 向Component传入参数并构建对象
export default connect(
    mapStateToProps,
    {
        addCount,
    },
)(App);

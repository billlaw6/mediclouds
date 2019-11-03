import React from 'react';
import { connect } from 'react-redux';
import { AppState } from './store';
import { addCount } from './store/actions';
import './App.css';

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

const mapStateToProps = (state: AppState) => ({
    count: state.count,
});

// export default App;
export default connect(
    mapStateToProps,
    {
        addCount,
    },
)(App);

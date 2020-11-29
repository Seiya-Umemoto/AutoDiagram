import React, { Component } from 'react';
import axios from 'axios'
import { Button, Spinner } from 'react-bootstrap';
import RecipeContainer from "./RecipeContainer";

class Menu extends Component {
    state = { 
        hits: [],
        isLoading: false,
    }

    activateSpinner =()=> {
        this.setState({
            hits:[],
            isLoading:true,
        })
    }

    deactivateSpinner =()=> {
        this.setState({isLoading:false})
    }

    fetchIngredients = () => {
        this.activateSpinner()
        axios.get('http://127.0.0.1:8000/api/images/', {
            headers: {
                'accept': 'application/json',
            }  
        })
        .then(resp=>{
            console.log(resp.data[0].classified)
            this.fetchRecipes(resp.data[0].classified)
        })
        .catch(err=>{
            console.log(err)
        })
    }

    fetchRecipes = (name) => {
        axios.get(`https://api.edamam.com/search?q=${name}&ingr=10&time=30&app_id=bb0e720d&app_key=043f045e14d2b7cf226ebf4323358470&`)
        .then(resp=>{
            this.setState({hits: resp.data.hits})
            // this.state.hits.forEach(element => {
            //     console.log(element.recipe)
            // });
        })
        .catch(err=>{
            console.log(err)
        })
        this.deactivateSpinner()
    }

    render() { 
        return ( 
            <div>
                <Button variant='info' size='lg' className='mt-3' onClick={this.fetchIngredients}>Recommend Menu</Button>

                {this.state.isLoading && 
                    <Spinner animation="border" role="status"></Spinner>
                }
                <RecipeContainer hits={this.state.hits} />
            </div>
        );
    }
}
 
export default Menu;
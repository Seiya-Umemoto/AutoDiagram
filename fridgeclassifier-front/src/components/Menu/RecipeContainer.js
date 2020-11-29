import React from 'react';
import Recipe from './Recipe';

const RecipeContainer = props => {

    const displayRecipes = () => {
        
        return props.hits.map(hit => {
            return <Recipe key={hit.recipe.uri} recipe={hit.recipe}/>;
        });
    };

    return (
        <>
            <p>Here are some recommended recipes</p>
            <section>{displayRecipes()}</section>
        </>
    );
};

export default RecipeContainer;
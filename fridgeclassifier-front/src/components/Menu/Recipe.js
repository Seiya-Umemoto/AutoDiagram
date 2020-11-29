import React from 'react';

const Recipe = (props) => {
    console.log("pass",props.recipe)
    return (
        <div>
            <p>{props.recipe.label}</p>
            <p>Calories: {props.recipe.calories}</p>
            <a href={props.recipe.url}>
            <img
                 src={props.recipe.image}
                 alt="Recipe"
            /></a>
        </div>
    );
};

export default Recipe;
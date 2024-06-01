import React from 'react';
import './App.css';

function WebsiteHead() {
  return (
    <div class="header">
      <h1>Clothing Sales Tracker</h1>
      <a href="https://github.com/Ethan-Lem05/Clothing-price-tracker">GitHub Repo</a>
    </div>
  );
}

function itemDisplay() {
  return (
    <div>
      
    </div>
  )
}

/**
 * Renders a dropdown component.
 *
 * @param {Object} props - The component props.
 * @param {string} props.id - The id of the dropdown element.
 * @param {Array} props.options - The options to be displayed in the dropdown.
 * @param {string} props.labelText - The label text for the dropdown.
 * @returns {JSX.Element} The rendered dropdown component.
 */
function DropDown({id,options,labelText}) {
  return (
    <span>
      <label htmlFor={id}> {labelText} </label>
      <select id={id}>
        {options.map((option) => {
          return <option key={option} value={option}> {option} </option>
        })}
      </select>
    </span>
  );
}

function Filter() {
  return (
    <span>
      <div className="filter">
        <form name="filter-form" method="POST" class="horizontal-bar">
          <DropDown id='price-range' options={['$0-50','$50-100','$100-150','$150-200','$200-250']} labelText='price range: '/>
          <span>
            <label for="garment-type">garment type: </label>
            <select>
              <option value=""> select a clothing type </option>
              <option value="Tops"> Tops </option>
              <option value="Bottoms"> Bottoms </option>
              <option value="Shoes"> Shoes </option>
              <option value="Accessories"> Accessories </option>
            </select>
          </span>
          <span>
            <label for="garment-type">garment type: </label>
            <select>
              <option value=""> select a clothing type </option>
              <option value="Tops"> Tops </option>
              <option value="Bottoms"> Bottoms </option>
              <option value="Shoes"> Shoes </option>
              <option value="Accessories"> Accessories </option>
            </select>
          </span>
          <button type='submit' class="button"> submit </button>
        </form>
      </div>
    </span>
  );
}

function operationButton() {
  return (
    <div></div>
  )
}

function searchBar() {
  return (
    <div></div>
  )
}

function popUpForm() {

}


function App() {
  return (
    <div className="App">
      <WebsiteHead />
      <Filter />
    </div>
  );
}

export default App;

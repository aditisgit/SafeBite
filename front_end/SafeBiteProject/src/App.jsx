import React, { useState } from 'react';
import './App.css';


function App() {
  const [activeTab, setActiveTab] = useState('adulteration');

  return (
    <div
      className="min-h-screen bg-cover bg-no-repeat bg-center"
      style={{ backgroundImage: "url('https://www.example.com/food-background.jpg')" }}
    >
      <div className="max-w-screen-xl mx-auto p-8">
        <header className="text-center">
          <h1 className="text-4xl font-bold text-green-600">
            Food Adulteration & Contamination Detection
          </h1>
          <p className="mt-2 text-green-500">
            Ensuring Food Safety with Modern Technology
          </p>
        </header>

        {/* Tabs */}
        <div className="mt-6 flex justify-center space-x-4">
          {['adulteration', 'contamination', 'safety'].map((tab) => (
            <button
              key={tab}
              className={`px-4 py-2 rounded-lg ${
                activeTab === tab
                  ? 'bg-green-500 text-white'
                  : 'bg-green-200 text-green-700'
              }`}
              onClick={() => setActiveTab(tab)}
            >
              {tab === 'adulteration' && 'Adulteration Prediction'}
              {tab === 'contamination' && 'Contaminant Level Prediction'}
              {tab === 'safety' && 'Safety Classification'}
            </button>
          ))}
        </div>

        {/* Content */}
        <div className="mt-8">
          {activeTab === 'adulteration' && <AdulterationPrediction />}
          {activeTab === 'contamination' && <ContaminantLevelPrediction />}
          {activeTab === 'safety' && <SafetyClassification />}
        </div>
      </div>
    </div>
  );
}

// Reusable Components
const FormContainer = ({ title, children }) => (
  <div className="bg-white p-6 rounded-lg shadow-lg border border-green-300">
    <h2 className="text-xl font-semibold mb-4 text-green-600">{title}</h2>
    <div className="space-y-4">{children}</div>
  </div>
);

const InputField = ({ label, placeholder }) => (
  <div>
    <label className="text-green-600 block">{label}:</label>
    <input
      className="w-full p-3 border border-green-200 rounded mt-2"
      type="text"
      placeholder={placeholder}
    />
  </div>
);

const SelectField = ({ label, options }) => (
  <div>
    <label className="text-green-600 block">{label}:</label>
    <select className="w-full p-3 border border-green-200 rounded mt-2">
      <option>Select {label}</option>
      {options.map((option, index) => (
        <option key={index}>{option}</option>
      ))}
    </select>
  </div>
);

const NumberField = ({ label }) => {
  const [value, setValue] = useState(0);
  return (
    <div>
      <label className="text-green-600 block">{label}:</label>
      <div className="flex mt-2">
        <input
          type="number"
          className="w-full p-3 border border-green-200 rounded-l"
          value={value}
          onChange={(e) => setValue(parseInt(e.target.value))}
        />
        <div className="flex flex-col">
          <button
            className="bg-green-300 px-2 rounded-tr hover:bg-green-400"
            onClick={() => setValue(value + 1)}
          >+</button>
          <button
            className="bg-green-300 px-2 rounded-br hover:bg-green-400"
            onClick={() => setValue(value - 1)}
          >−</button>
        </div>
      </div>
    </div>
  );
};

const SubmitButton = ({ label }) => (
  <button className="w-full bg-green-600 text-white p-3 rounded mt-4 hover:bg-green-700 transition-all">
    {label}
  </button>
);

// Pages
const AdulterationPrediction = () => (
  <FormContainer title="Adulteration Prediction">
    <SelectField
      label="Adulterant"
      options={[
        'Water', 'Sugar Syrup', 'Soapstone', 'Chalk Powder', 'Jaggery Syrup',
        'Salt Powder', 'Brick Powder', 'Metanill Yellow', 'Urea', 'Starch',
        'Detergent', 'Water', 'None'
      ]}
    />
    <SelectField
      label="Food Type"
      options={['Milk', 'Wheat', 'Honey', 'Chilli Powder', 'Turmeric']}
    />
    <NumberField label="Adulteration Level" />
    <SubmitButton label="Predict Adulteration" />
  </FormContainer>
);

const ContaminantLevelPrediction = () => (
  <FormContainer title="Contaminant Level Prediction">
    <SelectField
      label="County Name"
      options={[
        'Hong Kong SAR', 'Japan', 'China', 'Singapore', 'Thailand',
        'India', 'Republic of Korea', 'Indonesia'
      ]}
    />
    <SelectField
      label="Food Group Name"
      options={[
        'Legumes and Pulses', 'Fish and Seafood', 'Vegetable and Vegetable Products',
        'Starchy roots and tubers', 'Milk and dairy products',
        'Fruit and fruit products', 'Eggs and egg products'
      ]}
    />
    <InputField label="Enter Food Name" placeholder="Food Name" />
    <SelectField
      label="Contaminant Name"
      options={[
        'Ethyle carbamate', 'Cesium 134', 'Cesium 137', 'Iodine 131',
        'Cesium total', 'Dioxins(WHO TEFs)', 'Other'
      ]}
    />
    <SubmitButton label="Predict Contamination Level" />
  </FormContainer>
);

const SafetyClassification = () => (
  <FormContainer title="Safety Classification">
    <SelectField
      label="Food Group"
      options={[
        'Legumes and Pulses', 'Fish and Seafood', 'Vegetable and Vegetable Products',
        'Starchy roots and tubers', 'Milk and dairy products',
        'Fruit and fruit products', 'Eggs and egg products'
      ]}
    />
    <SelectField
      label="Contaminant"
      options={[
        'Ethyle carbamate', 'Cesium 134', 'Cesium 137', 'Iodine 131',
        'Cesium total', 'Dioxins(WHO TEFs)', 'Other'
      ]}
    />
    <NumberField label="Enter Quantity of Contaminant" />
    <SubmitButton label="Predict Safety" />
  </FormContainer>
);

export default App;

'use client';

import Link from 'next/link';
import React from 'react';
import Image from 'next/image';

export default function Page() {
  return (
    <div>
      {/* Hero Section with Background */}
      <div 
        className="min-h-screen relative bg-cover bg-center bg-fixed"
        style={{
          backgroundImage: "linear-gradient(rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)), url('https://images.unsplash.com/photo-1498837167922-ddd27525d352?ixlib=rb-4.0.3')",
        }}
      >
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 pb-16">
          <div className="text-center">
            <h1 className="text-5xl font-bold text-green-600 mb-6">
              SafeBite
            </h1>
            <p className="text-xl text-gray-600 mb-8">
              Your trusted companion in ensuring food safety through advanced detection technology
            </p>
            <Link 
              href="/category" 
              className="inline-block bg-green-600 text-white px-8 py-3 rounded-lg hover:bg-green-700 transition-colors"
            >
              Get Started
            </Link>
          </div>

          {/* Three White Info Bars */}
          <div className="mt-16 grid md:grid-cols-3 gap-6">
            <div className="bg-white shadow-md rounded-lg p-6 text-center">
              <h2 className="text-xl font-semibold text-green-700 mb-2">Food Safety</h2>
              <p className="text-gray-700">
                Ensuring the food you eat is free from harmful contaminants is our top priority. We help you stay informed and protected.
              </p>
            </div>
            <div className="bg-white shadow-md rounded-lg p-6 text-center">
              <h2 className="text-xl font-semibold text-green-700 mb-2">Adulteration Risks</h2>
              <p className="text-gray-700">
                From synthetic additives to harmful preservatives, adulteration is real. SafeBite helps you detect and understand these risks.
              </p>
            </div>
            <div className="bg-white shadow-md rounded-lg p-6 text-center">
              <h2 className="text-xl font-semibold text-green-700 mb-2">Our Mission</h2>
              <p className="text-gray-700">
                Empowering consumers with easy-to-use AI tools to analyze and verify food quality — knowledge is safety.
              </p>
            </div>
          </div>

        </div>
      </div>

      {/* Rest of the sections */}
      {/* ...existing code for Features Section... */}
      {/* ...existing code for How It Works Section... */}
      {/* ...existing code for Footer... */}
    </div>
  );
}

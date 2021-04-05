{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6bed9c49",
   "metadata": {},
   "outputs": [],
   "source": [
    "# pages/urls.py\n",
    "from django.urls import path\n",
    "from .views import homePageView\n",
    "\n",
    "urlpatterns = [\n",
    "    path('', homePageView, name='home'),\n",
    "]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

from flask import Blueprint, request, render_template, url_for, redirect, current_app, session
import movie.adapters.repository as repo
from movie.adapters.memory_repository import save_reviews_to_disk, remove_review_from_disk
from movie.authentication.authentication import login_required
from movie.domainmodels.movie import Review
from movie.reviews.review_form import MovieReviewForm
from movie.util.constants import REVIEW_BP, REVIEW_ENDPOINT, REMOVE_REVIEW_ENDPOINT

review_blueprint = Blueprint(REVIEW_BP, __name__)


@review_blueprint.route('/' + REVIEW_ENDPOINT, methods=['GET', 'POST'])
@login_required
def add_review():
    forming = MovieReviewForm()
    id_movies = request.args.get('movie_id')
    movie = repo.repo_instance.get_movie_by_id(id_movies)
    no_value = None
    if movie is no_value:
        return redirect(url_for('home_bp.home'))

    elif forming.validate_on_submit():
        to_rate = int(forming.rating.data)
        to_comment = forming.review_text.data
        to_review = Review(movie, session['username'], to_comment, to_rate)
        movie.add_review(to_review)
        save_reviews_to_disk(current_app.config['REVIEW_DATA_PATH'], to_review)

        return render_template('movie/movie_info.html', movie=movie, )

    else:
        return render_template('review/add_review.html', form=forming, movie=movie)


@review_blueprint.route('/' + REMOVE_REVIEW_ENDPOINT, methods=['GET'])
@login_required
def remove_review():
    id_movies = request.args.get('movie_id')
    movie = repo.repo_instance.get_movie_by_id(id_movies)
    review_id = request.args.get('review_id')
    movie.remove_review_by_id(review_id)
    remove_review_from_disk(current_app.config['REVIEW_DATA_PATH'], review_id)
    return render_template('movie/movie_info.html', movie=movie)




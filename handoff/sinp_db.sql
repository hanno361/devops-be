--
-- PostgreSQL database dump
--

\restrict we0hsjrkVai2ikttBdS8pXwjU00Bf7VIQpzbg5LqEvUUK7gNI0HYRZeibKbcgLn

-- Dumped from database version 16.13
-- Dumped by pg_dump version 16.13

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE IF EXISTS ONLY public.wishlist_wishlistitem DROP CONSTRAINT IF EXISTS wishlist_wishlistitem_user_id_e2483288_fk_accounts_user_id;
ALTER TABLE IF EXISTS ONLY public.wishlist_wishlistitem DROP CONSTRAINT IF EXISTS wishlist_wishlistitem_product_id_8309716a_fk_catalog_product_id;
ALTER TABLE IF EXISTS ONLY public.orders_orderitem DROP CONSTRAINT IF EXISTS orders_orderitem_product_id_afe4254a_fk_catalog_product_id;
ALTER TABLE IF EXISTS ONLY public.orders_orderitem DROP CONSTRAINT IF EXISTS orders_orderitem_order_id_fe61a34d_fk_orders_order_id;
ALTER TABLE IF EXISTS ONLY public.orders_order DROP CONSTRAINT IF EXISTS orders_order_user_id_e9b59eb1_fk_accounts_user_id;
ALTER TABLE IF EXISTS ONLY public.home_bannerfeature DROP CONSTRAINT IF EXISTS home_bannerfeature_banner_id_d723305c_fk_home_banner_id;
ALTER TABLE IF EXISTS ONLY public.django_admin_log DROP CONSTRAINT IF EXISTS django_admin_log_user_id_c564eba6_fk_accounts_user_id;
ALTER TABLE IF EXISTS ONLY public.django_admin_log DROP CONSTRAINT IF EXISTS django_admin_log_content_type_id_c4bce8eb_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.catalog_productimage DROP CONSTRAINT IF EXISTS catalog_productimage_product_id_1f42dd8c_fk_catalog_product_id;
ALTER TABLE IF EXISTS ONLY public.catalog_product DROP CONSTRAINT IF EXISTS catalog_product_category_id_35bf920b_fk_catalog_category_id;
ALTER TABLE IF EXISTS ONLY public.catalog_product DROP CONSTRAINT IF EXISTS catalog_product_brand_id_bb0c7890_fk_catalog_brand_id;
ALTER TABLE IF EXISTS ONLY public.cart_cartitem DROP CONSTRAINT IF EXISTS cart_cartitem_product_id_b24e265a_fk_catalog_product_id;
ALTER TABLE IF EXISTS ONLY public.cart_cartitem DROP CONSTRAINT IF EXISTS cart_cartitem_cart_id_370ad265_fk_cart_cart_id;
ALTER TABLE IF EXISTS ONLY public.cart_cart DROP CONSTRAINT IF EXISTS cart_cart_user_id_9b4220b9_fk_accounts_user_id;
ALTER TABLE IF EXISTS ONLY public.blog_blogpost_tags DROP CONSTRAINT IF EXISTS blog_blogpost_tags_blogtag_id_15bead90_fk_blog_blogtag_id;
ALTER TABLE IF EXISTS ONLY public.blog_blogpost_tags DROP CONSTRAINT IF EXISTS blog_blogpost_tags_blogpost_id_cdcddf6c_fk_blog_blogpost_id;
ALTER TABLE IF EXISTS ONLY public.blog_blogpost DROP CONSTRAINT IF EXISTS blog_blogpost_category_id_0e9835dd_fk_blog_blogcategory_id;
ALTER TABLE IF EXISTS ONLY public.blog_blogpost DROP CONSTRAINT IF EXISTS blog_blogpost_author_id_ffcc150f_fk_accounts_user_id;
ALTER TABLE IF EXISTS ONLY public.auth_permission DROP CONSTRAINT IF EXISTS auth_permission_content_type_id_2f476e4b_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.auth_group_permissions DROP CONSTRAINT IF EXISTS auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
ALTER TABLE IF EXISTS ONLY public.auth_group_permissions DROP CONSTRAINT IF EXISTS auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
ALTER TABLE IF EXISTS ONLY public.accounts_user_user_permissions DROP CONSTRAINT IF EXISTS accounts_user_user_p_user_id_e4f0a161_fk_accounts_;
ALTER TABLE IF EXISTS ONLY public.accounts_user_user_permissions DROP CONSTRAINT IF EXISTS accounts_user_user_p_permission_id_113bb443_fk_auth_perm;
ALTER TABLE IF EXISTS ONLY public.accounts_user_groups DROP CONSTRAINT IF EXISTS accounts_user_groups_user_id_52b62117_fk_accounts_user_id;
ALTER TABLE IF EXISTS ONLY public.accounts_user_groups DROP CONSTRAINT IF EXISTS accounts_user_groups_group_id_bd11a704_fk_auth_group_id;
DROP INDEX IF EXISTS public.wishlist_wishlistitem_user_id_e2483288;
DROP INDEX IF EXISTS public.wishlist_wishlistitem_product_id_8309716a;
DROP INDEX IF EXISTS public.orders_orderitem_product_id_afe4254a;
DROP INDEX IF EXISTS public.orders_orderitem_order_id_fe61a34d;
DROP INDEX IF EXISTS public.orders_order_user_id_e9b59eb1;
DROP INDEX IF EXISTS public.orders_order_number_abc9e0f2_like;
DROP INDEX IF EXISTS public.home_bannerfeature_banner_id_d723305c;
DROP INDEX IF EXISTS public.django_session_session_key_c0390e0f_like;
DROP INDEX IF EXISTS public.django_session_expire_date_a5c62663;
DROP INDEX IF EXISTS public.django_admin_log_user_id_c564eba6;
DROP INDEX IF EXISTS public.django_admin_log_content_type_id_c4bce8eb;
DROP INDEX IF EXISTS public.catalog_productimage_product_id_1f42dd8c;
DROP INDEX IF EXISTS public.catalog_product_slug_f37848b0_like;
DROP INDEX IF EXISTS public.catalog_product_sku_5c54c070_like;
DROP INDEX IF EXISTS public.catalog_product_category_id_35bf920b;
DROP INDEX IF EXISTS public.catalog_product_brand_id_bb0c7890;
DROP INDEX IF EXISTS public.catalog_pro_slug_2b1eb6_idx;
DROP INDEX IF EXISTS public.catalog_pro_is_acti_e6e001_idx;
DROP INDEX IF EXISTS public.catalog_category_slug_dbf63ad0_like;
DROP INDEX IF EXISTS public.catalog_category_name_fdc3466c_like;
DROP INDEX IF EXISTS public.catalog_brand_slug_988c8dbc_like;
DROP INDEX IF EXISTS public.catalog_brand_name_ea62c47f_like;
DROP INDEX IF EXISTS public.cart_cartitem_product_id_b24e265a;
DROP INDEX IF EXISTS public.cart_cartitem_cart_id_370ad265;
DROP INDEX IF EXISTS public.blog_blogtag_slug_eecf3988_like;
DROP INDEX IF EXISTS public.blog_blogtag_name_fdf4eaf8_like;
DROP INDEX IF EXISTS public.blog_blogpost_tags_blogtag_id_15bead90;
DROP INDEX IF EXISTS public.blog_blogpost_tags_blogpost_id_cdcddf6c;
DROP INDEX IF EXISTS public.blog_blogpost_slug_9e84ade1_like;
DROP INDEX IF EXISTS public.blog_blogpost_category_id_0e9835dd;
DROP INDEX IF EXISTS public.blog_blogpost_author_id_ffcc150f;
DROP INDEX IF EXISTS public.blog_blogpo_status_9c1956_idx;
DROP INDEX IF EXISTS public.blog_blogpo_slug_361555_idx;
DROP INDEX IF EXISTS public.blog_blogcategory_slug_7996de7a_like;
DROP INDEX IF EXISTS public.blog_blogcategory_name_b5c23ee6_like;
DROP INDEX IF EXISTS public.auth_permission_content_type_id_2f476e4b;
DROP INDEX IF EXISTS public.auth_group_permissions_permission_id_84c5c92e;
DROP INDEX IF EXISTS public.auth_group_permissions_group_id_b120cbf9;
DROP INDEX IF EXISTS public.auth_group_name_a6ea08ec_like;
DROP INDEX IF EXISTS public.accounts_user_username_6088629e_like;
DROP INDEX IF EXISTS public.accounts_user_user_permissions_user_id_e4f0a161;
DROP INDEX IF EXISTS public.accounts_user_user_permissions_permission_id_113bb443;
DROP INDEX IF EXISTS public.accounts_user_groups_user_id_52b62117;
DROP INDEX IF EXISTS public.accounts_user_groups_group_id_bd11a704;
DROP INDEX IF EXISTS public.accounts_user_email_b2644a56_like;
ALTER TABLE IF EXISTS ONLY public.wishlist_wishlistitem DROP CONSTRAINT IF EXISTS wishlist_wishlistitem_user_id_product_id_fc088002_uniq;
ALTER TABLE IF EXISTS ONLY public.wishlist_wishlistitem DROP CONSTRAINT IF EXISTS wishlist_wishlistitem_pkey;
ALTER TABLE IF EXISTS ONLY public.pages_teammember DROP CONSTRAINT IF EXISTS pages_teammember_pkey;
ALTER TABLE IF EXISTS ONLY public.pages_faq DROP CONSTRAINT IF EXISTS pages_faq_pkey;
ALTER TABLE IF EXISTS ONLY public.pages_contactmessage DROP CONSTRAINT IF EXISTS pages_contactmessage_pkey;
ALTER TABLE IF EXISTS ONLY public.pages_aboutpage DROP CONSTRAINT IF EXISTS pages_aboutpage_pkey;
ALTER TABLE IF EXISTS ONLY public.orders_orderitem DROP CONSTRAINT IF EXISTS orders_orderitem_pkey;
ALTER TABLE IF EXISTS ONLY public.orders_order DROP CONSTRAINT IF EXISTS orders_order_pkey;
ALTER TABLE IF EXISTS ONLY public.orders_order DROP CONSTRAINT IF EXISTS orders_order_number_key;
ALTER TABLE IF EXISTS ONLY public.home_heroslide DROP CONSTRAINT IF EXISTS home_heroslide_pkey;
ALTER TABLE IF EXISTS ONLY public.home_featuredproduct DROP CONSTRAINT IF EXISTS home_featuredproduct_pkey;
ALTER TABLE IF EXISTS ONLY public.home_bannerfeature DROP CONSTRAINT IF EXISTS home_bannerfeature_pkey;
ALTER TABLE IF EXISTS ONLY public.home_banner DROP CONSTRAINT IF EXISTS home_banner_pkey;
ALTER TABLE IF EXISTS ONLY public.django_session DROP CONSTRAINT IF EXISTS django_session_pkey;
ALTER TABLE IF EXISTS ONLY public.django_migrations DROP CONSTRAINT IF EXISTS django_migrations_pkey;
ALTER TABLE IF EXISTS ONLY public.django_content_type DROP CONSTRAINT IF EXISTS django_content_type_pkey;
ALTER TABLE IF EXISTS ONLY public.django_content_type DROP CONSTRAINT IF EXISTS django_content_type_app_label_model_76bd3d3b_uniq;
ALTER TABLE IF EXISTS ONLY public.django_admin_log DROP CONSTRAINT IF EXISTS django_admin_log_pkey;
ALTER TABLE IF EXISTS ONLY public.catalog_productimage DROP CONSTRAINT IF EXISTS catalog_productimage_pkey;
ALTER TABLE IF EXISTS ONLY public.catalog_product DROP CONSTRAINT IF EXISTS catalog_product_slug_key;
ALTER TABLE IF EXISTS ONLY public.catalog_product DROP CONSTRAINT IF EXISTS catalog_product_sku_key;
ALTER TABLE IF EXISTS ONLY public.catalog_product DROP CONSTRAINT IF EXISTS catalog_product_pkey;
ALTER TABLE IF EXISTS ONLY public.catalog_category DROP CONSTRAINT IF EXISTS catalog_category_slug_key;
ALTER TABLE IF EXISTS ONLY public.catalog_category DROP CONSTRAINT IF EXISTS catalog_category_pkey;
ALTER TABLE IF EXISTS ONLY public.catalog_category DROP CONSTRAINT IF EXISTS catalog_category_name_key;
ALTER TABLE IF EXISTS ONLY public.catalog_brand DROP CONSTRAINT IF EXISTS catalog_brand_slug_key;
ALTER TABLE IF EXISTS ONLY public.catalog_brand DROP CONSTRAINT IF EXISTS catalog_brand_pkey;
ALTER TABLE IF EXISTS ONLY public.catalog_brand DROP CONSTRAINT IF EXISTS catalog_brand_name_key;
ALTER TABLE IF EXISTS ONLY public.cart_cartitem DROP CONSTRAINT IF EXISTS cart_cartitem_pkey;
ALTER TABLE IF EXISTS ONLY public.cart_cartitem DROP CONSTRAINT IF EXISTS cart_cartitem_cart_id_product_id_53cce7c3_uniq;
ALTER TABLE IF EXISTS ONLY public.cart_cart DROP CONSTRAINT IF EXISTS cart_cart_user_id_key;
ALTER TABLE IF EXISTS ONLY public.cart_cart DROP CONSTRAINT IF EXISTS cart_cart_pkey;
ALTER TABLE IF EXISTS ONLY public.blog_blogtag DROP CONSTRAINT IF EXISTS blog_blogtag_slug_key;
ALTER TABLE IF EXISTS ONLY public.blog_blogtag DROP CONSTRAINT IF EXISTS blog_blogtag_pkey;
ALTER TABLE IF EXISTS ONLY public.blog_blogtag DROP CONSTRAINT IF EXISTS blog_blogtag_name_key;
ALTER TABLE IF EXISTS ONLY public.blog_blogpost_tags DROP CONSTRAINT IF EXISTS blog_blogpost_tags_pkey;
ALTER TABLE IF EXISTS ONLY public.blog_blogpost_tags DROP CONSTRAINT IF EXISTS blog_blogpost_tags_blogpost_id_blogtag_id_3fcee7dc_uniq;
ALTER TABLE IF EXISTS ONLY public.blog_blogpost DROP CONSTRAINT IF EXISTS blog_blogpost_slug_key;
ALTER TABLE IF EXISTS ONLY public.blog_blogpost DROP CONSTRAINT IF EXISTS blog_blogpost_pkey;
ALTER TABLE IF EXISTS ONLY public.blog_blogcategory DROP CONSTRAINT IF EXISTS blog_blogcategory_slug_key;
ALTER TABLE IF EXISTS ONLY public.blog_blogcategory DROP CONSTRAINT IF EXISTS blog_blogcategory_pkey;
ALTER TABLE IF EXISTS ONLY public.blog_blogcategory DROP CONSTRAINT IF EXISTS blog_blogcategory_name_key;
ALTER TABLE IF EXISTS ONLY public.auth_permission DROP CONSTRAINT IF EXISTS auth_permission_pkey;
ALTER TABLE IF EXISTS ONLY public.auth_permission DROP CONSTRAINT IF EXISTS auth_permission_content_type_id_codename_01ab375a_uniq;
ALTER TABLE IF EXISTS ONLY public.auth_group DROP CONSTRAINT IF EXISTS auth_group_pkey;
ALTER TABLE IF EXISTS ONLY public.auth_group_permissions DROP CONSTRAINT IF EXISTS auth_group_permissions_pkey;
ALTER TABLE IF EXISTS ONLY public.auth_group_permissions DROP CONSTRAINT IF EXISTS auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
ALTER TABLE IF EXISTS ONLY public.auth_group DROP CONSTRAINT IF EXISTS auth_group_name_key;
ALTER TABLE IF EXISTS ONLY public.accounts_user DROP CONSTRAINT IF EXISTS accounts_user_username_key;
ALTER TABLE IF EXISTS ONLY public.accounts_user_user_permissions DROP CONSTRAINT IF EXISTS accounts_user_user_permissions_pkey;
ALTER TABLE IF EXISTS ONLY public.accounts_user_user_permissions DROP CONSTRAINT IF EXISTS accounts_user_user_permi_user_id_permission_id_2ab516c2_uniq;
ALTER TABLE IF EXISTS ONLY public.accounts_user DROP CONSTRAINT IF EXISTS accounts_user_pkey;
ALTER TABLE IF EXISTS ONLY public.accounts_user_groups DROP CONSTRAINT IF EXISTS accounts_user_groups_user_id_group_id_59c0b32f_uniq;
ALTER TABLE IF EXISTS ONLY public.accounts_user_groups DROP CONSTRAINT IF EXISTS accounts_user_groups_pkey;
ALTER TABLE IF EXISTS ONLY public.accounts_user DROP CONSTRAINT IF EXISTS accounts_user_email_key;
DROP TABLE IF EXISTS public.wishlist_wishlistitem;
DROP TABLE IF EXISTS public.pages_teammember;
DROP TABLE IF EXISTS public.pages_faq;
DROP TABLE IF EXISTS public.pages_contactmessage;
DROP TABLE IF EXISTS public.pages_aboutpage;
DROP TABLE IF EXISTS public.orders_orderitem;
DROP TABLE IF EXISTS public.orders_order;
DROP TABLE IF EXISTS public.home_heroslide;
DROP TABLE IF EXISTS public.home_featuredproduct;
DROP TABLE IF EXISTS public.home_bannerfeature;
DROP TABLE IF EXISTS public.home_banner;
DROP TABLE IF EXISTS public.django_session;
DROP TABLE IF EXISTS public.django_migrations;
DROP TABLE IF EXISTS public.django_content_type;
DROP TABLE IF EXISTS public.django_admin_log;
DROP TABLE IF EXISTS public.catalog_productimage;
DROP TABLE IF EXISTS public.catalog_product;
DROP TABLE IF EXISTS public.catalog_category;
DROP TABLE IF EXISTS public.catalog_brand;
DROP TABLE IF EXISTS public.cart_cartitem;
DROP TABLE IF EXISTS public.cart_cart;
DROP TABLE IF EXISTS public.blog_blogtag;
DROP TABLE IF EXISTS public.blog_blogpost_tags;
DROP TABLE IF EXISTS public.blog_blogpost;
DROP TABLE IF EXISTS public.blog_blogcategory;
DROP TABLE IF EXISTS public.auth_permission;
DROP TABLE IF EXISTS public.auth_group_permissions;
DROP TABLE IF EXISTS public.auth_group;
DROP TABLE IF EXISTS public.accounts_user_user_permissions;
DROP TABLE IF EXISTS public.accounts_user_groups;
DROP TABLE IF EXISTS public.accounts_user;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: accounts_user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.accounts_user (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    email character varying(254) NOT NULL,
    phone character varying(32) NOT NULL
);


--
-- Name: accounts_user_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.accounts_user_groups (
    id bigint NOT NULL,
    user_id bigint NOT NULL,
    group_id integer NOT NULL
);


--
-- Name: accounts_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.accounts_user_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.accounts_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: accounts_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.accounts_user ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.accounts_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: accounts_user_user_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.accounts_user_user_permissions (
    id bigint NOT NULL,
    user_id bigint NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: accounts_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.accounts_user_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.accounts_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: blog_blogcategory; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.blog_blogcategory (
    id bigint NOT NULL,
    name character varying(120) NOT NULL,
    slug character varying(140) NOT NULL
);


--
-- Name: blog_blogcategory_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.blog_blogcategory ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.blog_blogcategory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: blog_blogpost; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.blog_blogpost (
    id bigint NOT NULL,
    title character varying(200) NOT NULL,
    slug character varying(220) NOT NULL,
    excerpt character varying(300) NOT NULL,
    body text NOT NULL,
    cover character varying(100),
    status character varying(16) NOT NULL,
    published_at timestamp with time zone,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    author_id bigint,
    category_id bigint NOT NULL,
    cover_url character varying(255) NOT NULL
);


--
-- Name: blog_blogpost_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.blog_blogpost ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.blog_blogpost_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: blog_blogpost_tags; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.blog_blogpost_tags (
    id bigint NOT NULL,
    blogpost_id bigint NOT NULL,
    blogtag_id bigint NOT NULL
);


--
-- Name: blog_blogpost_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.blog_blogpost_tags ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.blog_blogpost_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: blog_blogtag; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.blog_blogtag (
    id bigint NOT NULL,
    name character varying(64) NOT NULL,
    slug character varying(80) NOT NULL
);


--
-- Name: blog_blogtag_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.blog_blogtag ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.blog_blogtag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: cart_cart; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.cart_cart (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    user_id bigint NOT NULL
);


--
-- Name: cart_cart_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.cart_cart ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.cart_cart_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: cart_cartitem; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.cart_cartitem (
    id bigint NOT NULL,
    quantity integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    cart_id bigint NOT NULL,
    product_id bigint NOT NULL,
    CONSTRAINT cart_cartitem_quantity_check CHECK ((quantity >= 0))
);


--
-- Name: cart_cartitem_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.cart_cartitem ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.cart_cartitem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: catalog_brand; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.catalog_brand (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    name character varying(120) NOT NULL,
    slug character varying(140) NOT NULL,
    logo character varying(100)
);


--
-- Name: catalog_brand_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.catalog_brand ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.catalog_brand_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: catalog_category; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.catalog_category (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    name character varying(120) NOT NULL,
    slug character varying(140) NOT NULL,
    description text NOT NULL
);


--
-- Name: catalog_category_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.catalog_category ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.catalog_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: catalog_product; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.catalog_product (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    name character varying(200) NOT NULL,
    slug character varying(220) NOT NULL,
    short_description character varying(300) NOT NULL,
    description text NOT NULL,
    price numeric(10,2) NOT NULL,
    sale_price numeric(10,2),
    sku character varying(64) NOT NULL,
    stock integer NOT NULL,
    is_featured boolean NOT NULL,
    is_active boolean NOT NULL,
    brand_id bigint,
    category_id bigint NOT NULL,
    image_url character varying(255) NOT NULL,
    CONSTRAINT catalog_product_stock_check CHECK ((stock >= 0))
);


--
-- Name: catalog_product_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.catalog_product ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.catalog_product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: catalog_productimage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.catalog_productimage (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    image character varying(100) NOT NULL,
    alt character varying(200) NOT NULL,
    is_primary boolean NOT NULL,
    "order" smallint NOT NULL,
    product_id bigint NOT NULL,
    CONSTRAINT catalog_productimage_order_check CHECK (("order" >= 0))
);


--
-- Name: catalog_productimage_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.catalog_productimage ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.catalog_productimage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- Name: home_banner; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.home_banner (
    id bigint NOT NULL,
    eyebrow character varying(120) NOT NULL,
    title character varying(200) NOT NULL,
    background_image character varying(255) NOT NULL,
    cta_label character varying(80) NOT NULL,
    cta_href character varying(255) NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


--
-- Name: home_banner_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.home_banner ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.home_banner_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: home_bannerfeature; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.home_bannerfeature (
    id bigint NOT NULL,
    icon character varying(80) NOT NULL,
    label character varying(120) NOT NULL,
    "order" smallint NOT NULL,
    banner_id bigint NOT NULL,
    CONSTRAINT home_bannerfeature_order_check CHECK (("order" >= 0))
);


--
-- Name: home_bannerfeature_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.home_bannerfeature ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.home_bannerfeature_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: home_featuredproduct; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.home_featuredproduct (
    id bigint NOT NULL,
    eyebrow character varying(120) NOT NULL,
    title character varying(200) NOT NULL,
    description text NOT NULL,
    image_src character varying(255) NOT NULL,
    image_alt character varying(200) NOT NULL,
    cta_href character varying(255) NOT NULL,
    image_right boolean NOT NULL,
    "order" smallint NOT NULL,
    is_active boolean NOT NULL,
    CONSTRAINT home_featuredproduct_order_check CHECK (("order" >= 0))
);


--
-- Name: home_featuredproduct_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.home_featuredproduct ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.home_featuredproduct_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: home_heroslide; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.home_heroslide (
    id bigint NOT NULL,
    bg character varying(255) NOT NULL,
    eyebrow character varying(120) NOT NULL,
    title character varying(200) NOT NULL,
    title_span character varying(200) NOT NULL,
    body text NOT NULL,
    cta_label character varying(80) NOT NULL,
    cta_href character varying(255) NOT NULL,
    "order" smallint NOT NULL,
    is_active boolean NOT NULL,
    CONSTRAINT home_heroslide_order_check CHECK (("order" >= 0))
);


--
-- Name: home_heroslide_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.home_heroslide ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.home_heroslide_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: orders_order; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.orders_order (
    id bigint NOT NULL,
    number character varying(32) NOT NULL,
    status character varying(16) NOT NULL,
    full_name character varying(200) NOT NULL,
    email character varying(254) NOT NULL,
    phone character varying(32) NOT NULL,
    address_line1 character varying(255) NOT NULL,
    address_line2 character varying(255) NOT NULL,
    city character varying(120) NOT NULL,
    postal_code character varying(32) NOT NULL,
    country character varying(120) NOT NULL,
    note text NOT NULL,
    subtotal numeric(12,2) NOT NULL,
    shipping_fee numeric(10,2) NOT NULL,
    total numeric(12,2) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    user_id bigint NOT NULL
);


--
-- Name: orders_order_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.orders_order ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.orders_order_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: orders_orderitem; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.orders_orderitem (
    id bigint NOT NULL,
    product_name character varying(200) NOT NULL,
    product_sku character varying(64) NOT NULL,
    unit_price numeric(10,2) NOT NULL,
    quantity integer NOT NULL,
    order_id bigint NOT NULL,
    product_id bigint,
    CONSTRAINT orders_orderitem_quantity_check CHECK ((quantity >= 0))
);


--
-- Name: orders_orderitem_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.orders_orderitem ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.orders_orderitem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: pages_aboutpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_aboutpage (
    id bigint NOT NULL,
    title character varying(200) NOT NULL,
    intro text NOT NULL,
    body text NOT NULL,
    cover character varying(100),
    updated_at timestamp with time zone NOT NULL
);


--
-- Name: pages_aboutpage_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.pages_aboutpage ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.pages_aboutpage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: pages_contactmessage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_contactmessage (
    id bigint NOT NULL,
    name character varying(120) NOT NULL,
    email character varying(254) NOT NULL,
    subject character varying(200) NOT NULL,
    message text NOT NULL,
    is_read boolean NOT NULL,
    created_at timestamp with time zone NOT NULL
);


--
-- Name: pages_contactmessage_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.pages_contactmessage ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.pages_contactmessage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: pages_faq; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_faq (
    id bigint NOT NULL,
    question character varying(300) NOT NULL,
    answer text NOT NULL,
    "order" smallint NOT NULL,
    is_active boolean NOT NULL,
    CONSTRAINT pages_faq_order_check CHECK (("order" >= 0))
);


--
-- Name: pages_faq_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.pages_faq ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.pages_faq_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: pages_teammember; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pages_teammember (
    id bigint NOT NULL,
    name character varying(120) NOT NULL,
    role character varying(120) NOT NULL,
    bio text NOT NULL,
    photo character varying(100),
    "order" smallint NOT NULL,
    CONSTRAINT pages_teammember_order_check CHECK (("order" >= 0))
);


--
-- Name: pages_teammember_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.pages_teammember ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.pages_teammember_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: wishlist_wishlistitem; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wishlist_wishlistitem (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    product_id bigint NOT NULL,
    user_id bigint NOT NULL
);


--
-- Name: wishlist_wishlistitem_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.wishlist_wishlistitem ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.wishlist_wishlistitem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: accounts_user; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.accounts_user (id, password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, email, phone) FROM stdin;
1	pbkdf2_sha256$720000$zUsiNQlvyisl65qVti92kP$6d+x4pglZiBA+OEjyP8dvTmuhFME2lMMofqJB4pUTMw=	\N	t	admin			t	t	2026-05-09 13:09:42.417005+00	admin@sinp.local	
\.


--
-- Data for Name: accounts_user_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.accounts_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: accounts_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.accounts_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add user	6	add_user
22	Can change user	6	change_user
23	Can delete user	6	delete_user
24	Can view user	6	view_user
25	Can add brand	7	add_brand
26	Can change brand	7	change_brand
27	Can delete brand	7	delete_brand
28	Can view brand	7	view_brand
29	Can add category	8	add_category
30	Can change category	8	change_category
31	Can delete category	8	delete_category
32	Can view category	8	view_category
33	Can add product	9	add_product
34	Can change product	9	change_product
35	Can delete product	9	delete_product
36	Can view product	9	view_product
37	Can add product image	10	add_productimage
38	Can change product image	10	change_productimage
39	Can delete product image	10	delete_productimage
40	Can view product image	10	view_productimage
41	Can add blog category	11	add_blogcategory
42	Can change blog category	11	change_blogcategory
43	Can delete blog category	11	delete_blogcategory
44	Can view blog category	11	view_blogcategory
45	Can add blog tag	12	add_blogtag
46	Can change blog tag	12	change_blogtag
47	Can delete blog tag	12	delete_blogtag
48	Can view blog tag	12	view_blogtag
49	Can add blog post	13	add_blogpost
50	Can change blog post	13	change_blogpost
51	Can delete blog post	13	delete_blogpost
52	Can view blog post	13	view_blogpost
53	Can add About page	14	add_aboutpage
54	Can change About page	14	change_aboutpage
55	Can delete About page	14	delete_aboutpage
56	Can view About page	14	view_aboutpage
57	Can add contact message	15	add_contactmessage
58	Can change contact message	15	change_contactmessage
59	Can delete contact message	15	delete_contactmessage
60	Can view contact message	15	view_contactmessage
61	Can add FAQ	16	add_faq
62	Can change FAQ	16	change_faq
63	Can delete FAQ	16	delete_faq
64	Can view FAQ	16	view_faq
65	Can add team member	17	add_teammember
66	Can change team member	17	change_teammember
67	Can delete team member	17	delete_teammember
68	Can view team member	17	view_teammember
69	Can add cart	18	add_cart
70	Can change cart	18	change_cart
71	Can delete cart	18	delete_cart
72	Can view cart	18	view_cart
73	Can add cart item	19	add_cartitem
74	Can change cart item	19	change_cartitem
75	Can delete cart item	19	delete_cartitem
76	Can view cart item	19	view_cartitem
77	Can add wishlist item	20	add_wishlistitem
78	Can change wishlist item	20	change_wishlistitem
79	Can delete wishlist item	20	delete_wishlistitem
80	Can view wishlist item	20	view_wishlistitem
81	Can add order	21	add_order
82	Can change order	21	change_order
83	Can delete order	21	delete_order
84	Can view order	21	view_order
85	Can add order item	22	add_orderitem
86	Can change order item	22	change_orderitem
87	Can delete order item	22	delete_orderitem
88	Can view order item	22	view_orderitem
89	Can add Banner	23	add_banner
90	Can change Banner	23	change_banner
91	Can delete Banner	23	delete_banner
92	Can view Banner	23	view_banner
93	Can add featured product	24	add_featuredproduct
94	Can change featured product	24	change_featuredproduct
95	Can delete featured product	24	delete_featuredproduct
96	Can view featured product	24	view_featuredproduct
97	Can add hero slide	25	add_heroslide
98	Can change hero slide	25	change_heroslide
99	Can delete hero slide	25	delete_heroslide
100	Can view hero slide	25	view_heroslide
101	Can add banner feature	26	add_bannerfeature
102	Can change banner feature	26	change_bannerfeature
103	Can delete banner feature	26	delete_bannerfeature
104	Can view banner feature	26	view_bannerfeature
\.


--
-- Data for Name: blog_blogcategory; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.blog_blogcategory (id, name, slug) FROM stdin;
1	Notes & Stories	notes-stories
2	Behind the Bottle	behind-the-bottle
3	Care Guide	care-guide
\.


--
-- Data for Name: blog_blogpost; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.blog_blogpost (id, title, slug, excerpt, body, cover, status, published_at, created_at, updated_at, author_id, category_id, cover_url) FROM stdin;
1	How to Layer a Signature Scent	how-to-layer-a-signature-scent	Three rules for building a layered fragrance wardrobe.	Start with a clean base, build with a complementary mist, and finish with a single spritz of EDP on pulse points...		published	2026-05-09 13:09:42.596896+00	2026-05-09 13:09:42.597863+00	2026-05-09 13:09:42.597865+00	1	3	/images/blog1.webp
2	Inside the Atelier: Distilling Damask Rose	inside-the-atelier-distilling-damask-rose	A morning at the distillery in Isparta.	Every spring our team travels to Isparta where Damask rose is harvested before dawn...		published	2026-05-06 13:09:42.600854+00	2026-05-09 13:09:42.601362+00	2026-05-09 13:09:42.601366+00	1	2	/images/blog2.webp
3	Why Oud is the King of Notes	why-oud-is-the-king-of-notes	From agarwood resin to your bottle.	Oud is the resinous heartwood of the agarwood tree. Its formation is a slow, rare process...		published	2026-05-03 13:09:42.602931+00	2026-05-09 13:09:42.603427+00	2026-05-09 13:09:42.603429+00	1	1	/images/blog3.webp
4	Summer Scent Survival Kit	summer-scent-survival-kit	Light EDTs, body mists and a refreshing trick.	Heat changes how we wear scent. Swap heavy parfums for crisp citrus EDTs...		published	2026-04-30 13:09:42.604894+00	2026-05-09 13:09:42.605374+00	2026-05-09 13:09:42.605377+00	1	3	/images/blog4.webp
5	Notes 101: Top, Heart, Base	notes-101-top-heart-base	A 3-minute guide to fragrance pyramids.	Top notes evaporate first — citrus, herbs, light spice. Heart notes are the soul of a scent...		published	2026-04-27 13:09:42.606889+00	2026-05-09 13:09:42.607378+00	2026-05-09 13:09:42.60738+00	1	1	/images/blog1.webp
\.


--
-- Data for Name: blog_blogpost_tags; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.blog_blogpost_tags (id, blogpost_id, blogtag_id) FROM stdin;
1	1	1
2	1	5
3	2	2
4	3	3
5	4	4
6	4	5
7	5	1
\.


--
-- Data for Name: blog_blogtag; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.blog_blogtag (id, name, slug) FROM stdin;
1	fragrance	fragrance
2	rose	rose
3	oud	oud
4	summer	summer
5	tutorial	tutorial
\.


--
-- Data for Name: cart_cart; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.cart_cart (id, created_at, updated_at, user_id) FROM stdin;
\.


--
-- Data for Name: cart_cartitem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.cart_cartitem (id, quantity, created_at, updated_at, cart_id, product_id) FROM stdin;
\.


--
-- Data for Name: catalog_brand; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.catalog_brand (id, created_at, updated_at, name, slug, logo) FROM stdin;
1	2026-05-09 13:09:42.57157+00	2026-05-09 13:09:42.571573+00	Sinp Atelier	sinp-atelier	
2	2026-05-09 13:09:42.57248+00	2026-05-09 13:09:42.572484+00	Sinp Noir	sinp-noir	
3	2026-05-09 13:09:42.573812+00	2026-05-09 13:09:42.573816+00	Sinp Aqua	sinp-aqua	
\.


--
-- Data for Name: catalog_category; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.catalog_category (id, created_at, updated_at, name, slug, description) FROM stdin;
1	2026-05-09 13:09:42.56768+00	2026-05-09 13:09:42.567689+00	Eau de Parfum	eau-de-parfum	Long-lasting parfum collection.
2	2026-05-09 13:09:42.568901+00	2026-05-09 13:09:42.568905+00	Eau de Toilette	eau-de-toilette	Lighter toilette scents for daytime.
3	2026-05-09 13:09:42.569704+00	2026-05-09 13:09:42.569709+00	Body Care	body-care	Body sprays, lotions and care products.
4	2026-05-09 13:09:42.57045+00	2026-05-09 13:09:42.570454+00	Gift Sets	gift-sets	Curated gift bundles.
\.


--
-- Data for Name: catalog_product; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.catalog_product (id, created_at, updated_at, name, slug, short_description, description, price, sale_price, sku, stock, is_featured, is_active, brand_id, category_id, image_url) FROM stdin;
1	2026-05-09 13:09:42.575942+00	2026-05-09 13:09:42.575945+00	Velvet Rose Eau de Parfum 50ml	velvet-rose-eau-de-parfum-50ml	Romantic rose with a smoky musk base.	A signature scent built on Damask rose, oud and warm amber. Hand-bottled in Grasse and aged for 90 days for depth.	129.00	99.00	SNP-EDP-VR50	25	t	t	1	1	/images/product1.webp
2	2026-05-09 13:09:42.577932+00	2026-05-09 13:09:42.577936+00	Black Vetiver Eau de Parfum 75ml	black-vetiver-eau-de-parfum-75ml	Deep vetiver with leather facets.	Smoked vetiver, Haitian roots and aged leather make this a bold, modern parfum.	159.00	\N	SNP-EDP-BV75	18	t	t	2	1	/images/product2.webp
3	2026-05-09 13:09:42.579272+00	2026-05-09 13:09:42.579276+00	Aqua Citrus Eau de Toilette 100ml	aqua-citrus-eau-de-toilette-100ml	Bright bergamot and sea salt.	A fresh splash of bergamot, mandarin and sea minerals — perfect for sunny days.	79.00	59.00	SNP-EDT-AC100	40	f	t	3	2	/images/product3.webp
4	2026-05-09 13:09:42.580759+00	2026-05-09 13:09:42.580762+00	Cedar Smoke EDP 50ml	cedar-smoke-edp-50ml	Smoky cedar with warm spice.	Cedarwood smoke layered with cardamom and saffron.	119.00	\N	SNP-EDP-CS50	22	f	t	2	1	/images/product4.webp
5	2026-05-09 13:09:42.582379+00	2026-05-09 13:09:42.582384+00	Body Mist — Lily Garden 200ml	body-mist-lily-garden-200ml	Soft daily body mist.	Lily, white tea and sandalwood in a hydrating mist.	29.00	\N	SNP-BM-LG200	60	f	t	1	3	/images/product5.webp
6	2026-05-09 13:09:42.583806+00	2026-05-09 13:09:42.58381+00	Discovery Set — 5x10ml	discovery-set-5x10ml	Five signature scents in travel sizes.	Discover the Sinp range in 5x10ml refillable atomisers.	69.00	55.00	SNP-GIFT-DS5	35	t	t	1	4	/images/product1_1.webp
7	2026-05-09 13:09:42.585233+00	2026-05-09 13:09:42.585236+00	Amber Oud EDP 100ml	amber-oud-edp-100ml	Resinous amber and aged oud.	A statement parfum centred on Cambodian oud, labdanum and benzoin.	189.00	\N	SNP-EDP-AO100	12	t	t	1	1	/images/product2_1.webp
8	2026-05-09 13:09:42.586634+00	2026-05-09 13:09:42.586638+00	Body Lotion — Velvet Rose 250ml	body-lotion-velvet-rose-250ml	Layer with the Velvet Rose parfum.	Rich shea-butter lotion infused with the Velvet Rose accord.	34.00	\N	SNP-BL-VR250	50	f	t	1	3	/images/product3_1.webp
9	2026-05-09 13:09:42.587993+00	2026-05-09 13:09:42.587997+00	Gift Set — His & Hers Duo	gift-set-his-hers-duo	Velvet Rose and Black Vetiver paired.	Two of our signature parfums boxed together.	239.00	199.00	SNP-GIFT-HH	14	t	t	1	4	/images/product4_1.webp
10	2026-05-09 13:09:42.589406+00	2026-05-09 13:09:42.58941+00	Aqua Citrus EDT 50ml Travel	aqua-citrus-edt-50ml-travel	Pocket-sized fresh splash.	Travel-sized 50ml of our best-selling Aqua Citrus EDT.	49.00	\N	SNP-EDT-AC50	45	f	t	3	2	/images/product5_1.webp
\.


--
-- Data for Name: catalog_productimage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.catalog_productimage (id, created_at, updated_at, image, alt, is_primary, "order", product_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	accounts	user
7	catalog	brand
8	catalog	category
9	catalog	product
10	catalog	productimage
11	blog	blogcategory
12	blog	blogtag
13	blog	blogpost
14	pages	aboutpage
15	pages	contactmessage
16	pages	faq
17	pages	teammember
18	cart	cart
19	cart	cartitem
20	wishlist	wishlistitem
21	orders	order
22	orders	orderitem
23	home	banner
24	home	featuredproduct
25	home	heroslide
26	home	bannerfeature
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2026-05-09 13:09:23.041337+00
2	contenttypes	0002_remove_content_type_name	2026-05-09 13:09:23.043841+00
3	auth	0001_initial	2026-05-09 13:09:23.05817+00
4	auth	0002_alter_permission_name_max_length	2026-05-09 13:09:23.060282+00
5	auth	0003_alter_user_email_max_length	2026-05-09 13:09:23.062247+00
6	auth	0004_alter_user_username_opts	2026-05-09 13:09:23.064122+00
7	auth	0005_alter_user_last_login_null	2026-05-09 13:09:23.065985+00
8	auth	0006_require_contenttypes_0002	2026-05-09 13:09:23.066499+00
9	auth	0007_alter_validators_add_error_messages	2026-05-09 13:09:23.06822+00
10	auth	0008_alter_user_username_max_length	2026-05-09 13:09:23.070104+00
11	auth	0009_alter_user_last_name_max_length	2026-05-09 13:09:23.072071+00
12	auth	0010_alter_group_name_max_length	2026-05-09 13:09:23.074551+00
13	auth	0011_update_proxy_permissions	2026-05-09 13:09:23.076419+00
14	auth	0012_alter_user_first_name_max_length	2026-05-09 13:09:23.078885+00
15	accounts	0001_initial	2026-05-09 13:09:23.094574+00
16	admin	0001_initial	2026-05-09 13:09:23.102378+00
17	admin	0002_logentry_remove_auto_add	2026-05-09 13:09:23.104888+00
18	admin	0003_logentry_add_action_flag_choices	2026-05-09 13:09:23.107248+00
19	blog	0001_initial	2026-05-09 13:09:23.129772+00
20	blog	0002_blogpost_cover_url	2026-05-09 13:09:23.134184+00
21	catalog	0001_initial	2026-05-09 13:09:23.160653+00
22	cart	0001_initial	2026-05-09 13:09:23.176077+00
23	catalog	0002_product_image_url	2026-05-09 13:09:23.179035+00
24	home	0001_initial	2026-05-09 13:09:23.19016+00
25	orders	0001_initial	2026-05-09 13:09:23.210016+00
26	orders	0002_alter_order_country_alter_orderitem_product_and_more	2026-05-09 13:09:23.227191+00
27	pages	0001_initial	2026-05-09 13:09:23.237188+00
28	sessions	0001_initial	2026-05-09 13:09:23.24211+00
29	wishlist	0001_initial	2026-05-09 13:09:23.253852+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: home_banner; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.home_banner (id, eyebrow, title, background_image, cta_label, cta_href, updated_at) FROM stdin;
1	Atelier story	Slow-batched parfums, honest ingredients.	/images/bg.webp	About Sinp	/about	2026-05-09 13:09:42.620854+00
\.


--
-- Data for Name: home_bannerfeature; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.home_bannerfeature (id, icon, label, "order", banner_id) FROM stdin;
1	leaf	Cruelty-free	0	1
2	globe	Worldwide shipping	1	1
3	shield	90-day aged	2	1
\.


--
-- Data for Name: home_featuredproduct; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.home_featuredproduct (id, eyebrow, title, description, image_src, image_alt, cta_href, image_right, "order", is_active) FROM stdin;
1	Best seller	Velvet Rose Eau de Parfum	Romantic Damask rose grounded by smoky musk.	/images/product1_3.webp	Velvet Rose bottle	/product/velvet-rose-eau-de-parfum-50ml	f	0	t
2	New	Aqua Citrus Eau de Toilette	A bright splash of bergamot and sea salt.	/images/product2_3.webp	Aqua Citrus bottle	/product/aqua-citrus-eau-de-toilette-100ml	t	1	t
\.


--
-- Data for Name: home_heroslide; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.home_heroslide (id, bg, eyebrow, title, title_span, body, cta_label, cta_href, "order", is_active) FROM stdin;
1	/images/slide1.webp	New collection	Discover the	Velvet Rose	Hand-batched in Grasse, aged ninety days for depth.	Shop now	/shop	0	t
2	/images/slide2.webp	Limited edition	Black	Vetiver	Smoked vetiver and aged leather — a bold statement.	Explore	/product/black-vetiver-eau-de-parfum-75ml	1	t
\.


--
-- Data for Name: orders_order; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.orders_order (id, number, status, full_name, email, phone, address_line1, address_line2, city, postal_code, country, note, subtotal, shipping_fee, total, created_at, updated_at, user_id) FROM stdin;
\.


--
-- Data for Name: orders_orderitem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.orders_orderitem (id, product_name, product_sku, unit_price, quantity, order_id, product_id) FROM stdin;
\.


--
-- Data for Name: pages_aboutpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_aboutpage (id, title, intro, body, cover, updated_at) FROM stdin;
1	About Sinp	A small atelier crafting modern parfums with old-world technique.	Sinp was founded in 2019 with a simple promise: build fragrances slowly, age them deeply, and bottle them honestly. Every Sinp parfum is hand-batched in Grasse, France, and aged for a minimum of 90 days before it reaches you. We work directly with growers across Bulgaria, Türkiye and Madagascar to source rose, citrus and vanilla at peak quality.		2026-05-09 13:09:42.614083+00
\.


--
-- Data for Name: pages_contactmessage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_contactmessage (id, name, email, subject, message, is_read, created_at) FROM stdin;
\.


--
-- Data for Name: pages_faq; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_faq (id, question, answer, "order", is_active) FROM stdin;
1	Do you ship internationally?	Yes, we ship to most countries within 3-7 business days.	0	t
2	How can I track my order?	Once shipped, you'll receive a tracking link by email.	1	t
3	Are samples available?	Yes, the Discovery Set lets you try five signature scents.	2	t
4	Can I return a fragrance?	Unopened bottles can be returned within 14 days for a full refund.	3	t
5	How should I store my parfum?	Keep it in a cool, dark place — avoid direct sunlight and heat.	4	t
6	How long does an EDP last?	Most Sinp EDPs last 6-10 hours on skin and longer on clothing.	5	t
7	Are your products cruelty-free?	Absolutely. Sinp is fully cruelty-free and Leaping-Bunny certified.	6	t
\.


--
-- Data for Name: pages_teammember; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pages_teammember (id, name, role, bio, photo, "order") FROM stdin;
1	Aylin Demir	Master Perfumer	Trained in Grasse, leads the Sinp atelier.		0
2	Marco Russo	Lead Distiller	Manages our small-batch distillation process.		1
3	Sara Lin	Head of Experience	Designs every Sinp customer touchpoint.		2
\.


--
-- Data for Name: wishlist_wishlistitem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wishlist_wishlistitem (id, created_at, product_id, user_id) FROM stdin;
\.


--
-- Name: accounts_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.accounts_user_groups_id_seq', 1, false);


--
-- Name: accounts_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.accounts_user_id_seq', 1, true);


--
-- Name: accounts_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.accounts_user_user_permissions_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 104, true);


--
-- Name: blog_blogcategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.blog_blogcategory_id_seq', 3, true);


--
-- Name: blog_blogpost_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.blog_blogpost_id_seq', 5, true);


--
-- Name: blog_blogpost_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.blog_blogpost_tags_id_seq', 7, true);


--
-- Name: blog_blogtag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.blog_blogtag_id_seq', 5, true);


--
-- Name: cart_cart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.cart_cart_id_seq', 1, false);


--
-- Name: cart_cartitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.cart_cartitem_id_seq', 1, false);


--
-- Name: catalog_brand_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.catalog_brand_id_seq', 3, true);


--
-- Name: catalog_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.catalog_category_id_seq', 4, true);


--
-- Name: catalog_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.catalog_product_id_seq', 10, true);


--
-- Name: catalog_productimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.catalog_productimage_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 26, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 29, true);


--
-- Name: home_banner_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.home_banner_id_seq', 1, false);


--
-- Name: home_bannerfeature_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.home_bannerfeature_id_seq', 3, true);


--
-- Name: home_featuredproduct_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.home_featuredproduct_id_seq', 2, true);


--
-- Name: home_heroslide_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.home_heroslide_id_seq', 2, true);


--
-- Name: orders_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.orders_order_id_seq', 1, false);


--
-- Name: orders_orderitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.orders_orderitem_id_seq', 1, false);


--
-- Name: pages_aboutpage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pages_aboutpage_id_seq', 1, false);


--
-- Name: pages_contactmessage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pages_contactmessage_id_seq', 1, false);


--
-- Name: pages_faq_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pages_faq_id_seq', 7, true);


--
-- Name: pages_teammember_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pages_teammember_id_seq', 3, true);


--
-- Name: wishlist_wishlistitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wishlist_wishlistitem_id_seq', 1, false);


--
-- Name: accounts_user accounts_user_email_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user
    ADD CONSTRAINT accounts_user_email_key UNIQUE (email);


--
-- Name: accounts_user_groups accounts_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_groups
    ADD CONSTRAINT accounts_user_groups_pkey PRIMARY KEY (id);


--
-- Name: accounts_user_groups accounts_user_groups_user_id_group_id_59c0b32f_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_groups
    ADD CONSTRAINT accounts_user_groups_user_id_group_id_59c0b32f_uniq UNIQUE (user_id, group_id);


--
-- Name: accounts_user accounts_user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user
    ADD CONSTRAINT accounts_user_pkey PRIMARY KEY (id);


--
-- Name: accounts_user_user_permissions accounts_user_user_permi_user_id_permission_id_2ab516c2_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_user_permissions
    ADD CONSTRAINT accounts_user_user_permi_user_id_permission_id_2ab516c2_uniq UNIQUE (user_id, permission_id);


--
-- Name: accounts_user_user_permissions accounts_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_user_permissions
    ADD CONSTRAINT accounts_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: accounts_user accounts_user_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user
    ADD CONSTRAINT accounts_user_username_key UNIQUE (username);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: blog_blogcategory blog_blogcategory_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_blogcategory
    ADD CONSTRAINT blog_blogcategory_name_key UNIQUE (name);


--
-- Name: blog_blogcategory blog_blogcategory_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_blogcategory
    ADD CONSTRAINT blog_blogcategory_pkey PRIMARY KEY (id);


--
-- Name: blog_blogcategory blog_blogcategory_slug_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_blogcategory
    ADD CONSTRAINT blog_blogcategory_slug_key UNIQUE (slug);


--
-- Name: blog_blogpost blog_blogpost_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_blogpost
    ADD CONSTRAINT blog_blogpost_pkey PRIMARY KEY (id);


--
-- Name: blog_blogpost blog_blogpost_slug_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_blogpost
    ADD CONSTRAINT blog_blogpost_slug_key UNIQUE (slug);


--
-- Name: blog_blogpost_tags blog_blogpost_tags_blogpost_id_blogtag_id_3fcee7dc_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_blogpost_tags
    ADD CONSTRAINT blog_blogpost_tags_blogpost_id_blogtag_id_3fcee7dc_uniq UNIQUE (blogpost_id, blogtag_id);


--
-- Name: blog_blogpost_tags blog_blogpost_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_blogpost_tags
    ADD CONSTRAINT blog_blogpost_tags_pkey PRIMARY KEY (id);


--
-- Name: blog_blogtag blog_blogtag_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_blogtag
    ADD CONSTRAINT blog_blogtag_name_key UNIQUE (name);


--
-- Name: blog_blogtag blog_blogtag_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_blogtag
    ADD CONSTRAINT blog_blogtag_pkey PRIMARY KEY (id);


--
-- Name: blog_blogtag blog_blogtag_slug_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_blogtag
    ADD CONSTRAINT blog_blogtag_slug_key UNIQUE (slug);


--
-- Name: cart_cart cart_cart_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cart_cart
    ADD CONSTRAINT cart_cart_pkey PRIMARY KEY (id);


--
-- Name: cart_cart cart_cart_user_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cart_cart
    ADD CONSTRAINT cart_cart_user_id_key UNIQUE (user_id);


--
-- Name: cart_cartitem cart_cartitem_cart_id_product_id_53cce7c3_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cart_cartitem
    ADD CONSTRAINT cart_cartitem_cart_id_product_id_53cce7c3_uniq UNIQUE (cart_id, product_id);


--
-- Name: cart_cartitem cart_cartitem_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cart_cartitem
    ADD CONSTRAINT cart_cartitem_pkey PRIMARY KEY (id);


--
-- Name: catalog_brand catalog_brand_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.catalog_brand
    ADD CONSTRAINT catalog_brand_name_key UNIQUE (name);


--
-- Name: catalog_brand catalog_brand_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.catalog_brand
    ADD CONSTRAINT catalog_brand_pkey PRIMARY KEY (id);


--
-- Name: catalog_brand catalog_brand_slug_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.catalog_brand
    ADD CONSTRAINT catalog_brand_slug_key UNIQUE (slug);


--
-- Name: catalog_category catalog_category_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.catalog_category
    ADD CONSTRAINT catalog_category_name_key UNIQUE (name);


--
-- Name: catalog_category catalog_category_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.catalog_category
    ADD CONSTRAINT catalog_category_pkey PRIMARY KEY (id);


--
-- Name: catalog_category catalog_category_slug_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.catalog_category
    ADD CONSTRAINT catalog_category_slug_key UNIQUE (slug);


--
-- Name: catalog_product catalog_product_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.catalog_product
    ADD CONSTRAINT catalog_product_pkey PRIMARY KEY (id);


--
-- Name: catalog_product catalog_product_sku_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.catalog_product
    ADD CONSTRAINT catalog_product_sku_key UNIQUE (sku);


--
-- Name: catalog_product catalog_product_slug_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.catalog_product
    ADD CONSTRAINT catalog_product_slug_key UNIQUE (slug);


--
-- Name: catalog_productimage catalog_productimage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.catalog_productimage
    ADD CONSTRAINT catalog_productimage_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: home_banner home_banner_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.home_banner
    ADD CONSTRAINT home_banner_pkey PRIMARY KEY (id);


--
-- Name: home_bannerfeature home_bannerfeature_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.home_bannerfeature
    ADD CONSTRAINT home_bannerfeature_pkey PRIMARY KEY (id);


--
-- Name: home_featuredproduct home_featuredproduct_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.home_featuredproduct
    ADD CONSTRAINT home_featuredproduct_pkey PRIMARY KEY (id);


--
-- Name: home_heroslide home_heroslide_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.home_heroslide
    ADD CONSTRAINT home_heroslide_pkey PRIMARY KEY (id);


--
-- Name: orders_order orders_order_number_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.orders_order
    ADD CONSTRAINT orders_order_number_key UNIQUE (number);


--
-- Name: orders_order orders_order_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.orders_order
    ADD CONSTRAINT orders_order_pkey PRIMARY KEY (id);


--
-- Name: orders_orderitem orders_orderitem_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.orders_orderitem
    ADD CONSTRAINT orders_orderitem_pkey PRIMARY KEY (id);


--
-- Name: pages_aboutpage pages_aboutpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_aboutpage
    ADD CONSTRAINT pages_aboutpage_pkey PRIMARY KEY (id);


--
-- Name: pages_contactmessage pages_contactmessage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_contactmessage
    ADD CONSTRAINT pages_contactmessage_pkey PRIMARY KEY (id);


--
-- Name: pages_faq pages_faq_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_faq
    ADD CONSTRAINT pages_faq_pkey PRIMARY KEY (id);


--
-- Name: pages_teammember pages_teammember_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pages_teammember
    ADD CONSTRAINT pages_teammember_pkey PRIMARY KEY (id);


--
-- Name: wishlist_wishlistitem wishlist_wishlistitem_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wishlist_wishlistitem
    ADD CONSTRAINT wishlist_wishlistitem_pkey PRIMARY KEY (id);


--
-- Name: wishlist_wishlistitem wishlist_wishlistitem_user_id_product_id_fc088002_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wishlist_wishlistitem
    ADD CONSTRAINT wishlist_wishlistitem_user_id_product_id_fc088002_uniq UNIQUE (user_id, product_id);


--
-- Name: accounts_user_email_b2644a56_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_user_email_b2644a56_like ON public.accounts_user USING btree (email varchar_pattern_ops);


--
-- Name: accounts_user_groups_group_id_bd11a704; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_user_groups_group_id_bd11a704 ON public.accounts_user_groups USING btree (group_id);


--
-- Name: accounts_user_groups_user_id_52b62117; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_user_groups_user_id_52b62117 ON public.accounts_user_groups USING btree (user_id);


--
-- Name: accounts_user_user_permissions_permission_id_113bb443; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_user_user_permissions_permission_id_113bb443 ON public.accounts_user_user_permissions USING btree (permission_id);


--
-- Name: accounts_user_user_permissions_user_id_e4f0a161; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_user_user_permissions_user_id_e4f0a161 ON public.accounts_user_user_permissions USING btree (user_id);


--
-- Name: accounts_user_username_6088629e_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX accounts_user_username_6088629e_like ON public.accounts_user USING btree (username varchar_pattern_ops);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: blog_blogcategory_name_b5c23ee6_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX blog_blogcategory_name_b5c23ee6_like ON public.blog_blogcategory USING btree (name varchar_pattern_ops);


--
-- Name: blog_blogcategory_slug_7996de7a_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX blog_blogcategory_slug_7996de7a_like ON public.blog_blogcategory USING btree (slug varchar_pattern_ops);


--
-- Name: blog_blogpo_slug_361555_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX blog_blogpo_slug_361555_idx ON public.blog_blogpost USING btree (slug);


--
-- Name: blog_blogpo_status_9c1956_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX blog_blogpo_status_9c1956_idx ON public.blog_blogpost USING btree (status);


--
-- Name: blog_blogpost_author_id_ffcc150f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX blog_blogpost_author_id_ffcc150f ON public.blog_blogpost USING btree (author_id);


--
-- Name: blog_blogpost_category_id_0e9835dd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX blog_blogpost_category_id_0e9835dd ON public.blog_blogpost USING btree (category_id);


--
-- Name: blog_blogpost_slug_9e84ade1_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX blog_blogpost_slug_9e84ade1_like ON public.blog_blogpost USING btree (slug varchar_pattern_ops);


--
-- Name: blog_blogpost_tags_blogpost_id_cdcddf6c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX blog_blogpost_tags_blogpost_id_cdcddf6c ON public.blog_blogpost_tags USING btree (blogpost_id);


--
-- Name: blog_blogpost_tags_blogtag_id_15bead90; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX blog_blogpost_tags_blogtag_id_15bead90 ON public.blog_blogpost_tags USING btree (blogtag_id);


--
-- Name: blog_blogtag_name_fdf4eaf8_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX blog_blogtag_name_fdf4eaf8_like ON public.blog_blogtag USING btree (name varchar_pattern_ops);


--
-- Name: blog_blogtag_slug_eecf3988_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX blog_blogtag_slug_eecf3988_like ON public.blog_blogtag USING btree (slug varchar_pattern_ops);


--
-- Name: cart_cartitem_cart_id_370ad265; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cart_cartitem_cart_id_370ad265 ON public.cart_cartitem USING btree (cart_id);


--
-- Name: cart_cartitem_product_id_b24e265a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cart_cartitem_product_id_b24e265a ON public.cart_cartitem USING btree (product_id);


--
-- Name: catalog_brand_name_ea62c47f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX catalog_brand_name_ea62c47f_like ON public.catalog_brand USING btree (name varchar_pattern_ops);


--
-- Name: catalog_brand_slug_988c8dbc_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX catalog_brand_slug_988c8dbc_like ON public.catalog_brand USING btree (slug varchar_pattern_ops);


--
-- Name: catalog_category_name_fdc3466c_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX catalog_category_name_fdc3466c_like ON public.catalog_category USING btree (name varchar_pattern_ops);


--
-- Name: catalog_category_slug_dbf63ad0_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX catalog_category_slug_dbf63ad0_like ON public.catalog_category USING btree (slug varchar_pattern_ops);


--
-- Name: catalog_pro_is_acti_e6e001_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX catalog_pro_is_acti_e6e001_idx ON public.catalog_product USING btree (is_active, is_featured);


--
-- Name: catalog_pro_slug_2b1eb6_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX catalog_pro_slug_2b1eb6_idx ON public.catalog_product USING btree (slug);


--
-- Name: catalog_product_brand_id_bb0c7890; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX catalog_product_brand_id_bb0c7890 ON public.catalog_product USING btree (brand_id);


--
-- Name: catalog_product_category_id_35bf920b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX catalog_product_category_id_35bf920b ON public.catalog_product USING btree (category_id);


--
-- Name: catalog_product_sku_5c54c070_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX catalog_product_sku_5c54c070_like ON public.catalog_product USING btree (sku varchar_pattern_ops);


--
-- Name: catalog_product_slug_f37848b0_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX catalog_product_slug_f37848b0_like ON public.catalog_product USING btree (slug varchar_pattern_ops);


--
-- Name: catalog_productimage_product_id_1f42dd8c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX catalog_productimage_product_id_1f42dd8c ON public.catalog_productimage USING btree (product_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: home_bannerfeature_banner_id_d723305c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX home_bannerfeature_banner_id_d723305c ON public.home_bannerfeature USING btree (banner_id);


--
-- Name: orders_order_number_abc9e0f2_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX orders_order_number_abc9e0f2_like ON public.orders_order USING btree (number varchar_pattern_ops);


--
-- Name: orders_order_user_id_e9b59eb1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX orders_order_user_id_e9b59eb1 ON public.orders_order USING btree (user_id);


--
-- Name: orders_orderitem_order_id_fe61a34d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX orders_orderitem_order_id_fe61a34d ON public.orders_orderitem USING btree (order_id);


--
-- Name: orders_orderitem_product_id_afe4254a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX orders_orderitem_product_id_afe4254a ON public.orders_orderitem USING btree (product_id);


--
-- Name: wishlist_wishlistitem_product_id_8309716a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wishlist_wishlistitem_product_id_8309716a ON public.wishlist_wishlistitem USING btree (product_id);


--
-- Name: wishlist_wishlistitem_user_id_e2483288; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wishlist_wishlistitem_user_id_e2483288 ON public.wishlist_wishlistitem USING btree (user_id);


--
-- Name: accounts_user_groups accounts_user_groups_group_id_bd11a704_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_groups
    ADD CONSTRAINT accounts_user_groups_group_id_bd11a704_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_user_groups accounts_user_groups_user_id_52b62117_fk_accounts_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_groups
    ADD CONSTRAINT accounts_user_groups_user_id_52b62117_fk_accounts_user_id FOREIGN KEY (user_id) REFERENCES public.accounts_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_user_user_permissions accounts_user_user_p_permission_id_113bb443_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_user_permissions
    ADD CONSTRAINT accounts_user_user_p_permission_id_113bb443_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_user_user_permissions accounts_user_user_p_user_id_e4f0a161_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts_user_user_permissions
    ADD CONSTRAINT accounts_user_user_p_user_id_e4f0a161_fk_accounts_ FOREIGN KEY (user_id) REFERENCES public.accounts_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: blog_blogpost blog_blogpost_author_id_ffcc150f_fk_accounts_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_blogpost
    ADD CONSTRAINT blog_blogpost_author_id_ffcc150f_fk_accounts_user_id FOREIGN KEY (author_id) REFERENCES public.accounts_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: blog_blogpost blog_blogpost_category_id_0e9835dd_fk_blog_blogcategory_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_blogpost
    ADD CONSTRAINT blog_blogpost_category_id_0e9835dd_fk_blog_blogcategory_id FOREIGN KEY (category_id) REFERENCES public.blog_blogcategory(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: blog_blogpost_tags blog_blogpost_tags_blogpost_id_cdcddf6c_fk_blog_blogpost_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_blogpost_tags
    ADD CONSTRAINT blog_blogpost_tags_blogpost_id_cdcddf6c_fk_blog_blogpost_id FOREIGN KEY (blogpost_id) REFERENCES public.blog_blogpost(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: blog_blogpost_tags blog_blogpost_tags_blogtag_id_15bead90_fk_blog_blogtag_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_blogpost_tags
    ADD CONSTRAINT blog_blogpost_tags_blogtag_id_15bead90_fk_blog_blogtag_id FOREIGN KEY (blogtag_id) REFERENCES public.blog_blogtag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cart_cart cart_cart_user_id_9b4220b9_fk_accounts_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cart_cart
    ADD CONSTRAINT cart_cart_user_id_9b4220b9_fk_accounts_user_id FOREIGN KEY (user_id) REFERENCES public.accounts_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cart_cartitem cart_cartitem_cart_id_370ad265_fk_cart_cart_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cart_cartitem
    ADD CONSTRAINT cart_cartitem_cart_id_370ad265_fk_cart_cart_id FOREIGN KEY (cart_id) REFERENCES public.cart_cart(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cart_cartitem cart_cartitem_product_id_b24e265a_fk_catalog_product_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cart_cartitem
    ADD CONSTRAINT cart_cartitem_product_id_b24e265a_fk_catalog_product_id FOREIGN KEY (product_id) REFERENCES public.catalog_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: catalog_product catalog_product_brand_id_bb0c7890_fk_catalog_brand_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.catalog_product
    ADD CONSTRAINT catalog_product_brand_id_bb0c7890_fk_catalog_brand_id FOREIGN KEY (brand_id) REFERENCES public.catalog_brand(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: catalog_product catalog_product_category_id_35bf920b_fk_catalog_category_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.catalog_product
    ADD CONSTRAINT catalog_product_category_id_35bf920b_fk_catalog_category_id FOREIGN KEY (category_id) REFERENCES public.catalog_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: catalog_productimage catalog_productimage_product_id_1f42dd8c_fk_catalog_product_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.catalog_productimage
    ADD CONSTRAINT catalog_productimage_product_id_1f42dd8c_fk_catalog_product_id FOREIGN KEY (product_id) REFERENCES public.catalog_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_accounts_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_accounts_user_id FOREIGN KEY (user_id) REFERENCES public.accounts_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: home_bannerfeature home_bannerfeature_banner_id_d723305c_fk_home_banner_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.home_bannerfeature
    ADD CONSTRAINT home_bannerfeature_banner_id_d723305c_fk_home_banner_id FOREIGN KEY (banner_id) REFERENCES public.home_banner(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: orders_order orders_order_user_id_e9b59eb1_fk_accounts_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.orders_order
    ADD CONSTRAINT orders_order_user_id_e9b59eb1_fk_accounts_user_id FOREIGN KEY (user_id) REFERENCES public.accounts_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: orders_orderitem orders_orderitem_order_id_fe61a34d_fk_orders_order_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.orders_orderitem
    ADD CONSTRAINT orders_orderitem_order_id_fe61a34d_fk_orders_order_id FOREIGN KEY (order_id) REFERENCES public.orders_order(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: orders_orderitem orders_orderitem_product_id_afe4254a_fk_catalog_product_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.orders_orderitem
    ADD CONSTRAINT orders_orderitem_product_id_afe4254a_fk_catalog_product_id FOREIGN KEY (product_id) REFERENCES public.catalog_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wishlist_wishlistitem wishlist_wishlistitem_product_id_8309716a_fk_catalog_product_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wishlist_wishlistitem
    ADD CONSTRAINT wishlist_wishlistitem_product_id_8309716a_fk_catalog_product_id FOREIGN KEY (product_id) REFERENCES public.catalog_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wishlist_wishlistitem wishlist_wishlistitem_user_id_e2483288_fk_accounts_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wishlist_wishlistitem
    ADD CONSTRAINT wishlist_wishlistitem_user_id_e2483288_fk_accounts_user_id FOREIGN KEY (user_id) REFERENCES public.accounts_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

\unrestrict we0hsjrkVai2ikttBdS8pXwjU00Bf7VIQpzbg5LqEvUUK7gNI0HYRZeibKbcgLn

